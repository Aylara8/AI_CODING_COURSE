import os
import json
import random
import requests
from flask import Flask, render_template, redirect, url_for, request, flash, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from models import db, User, Profile, Resource
import uuid



app = Flask(__name__)

# --- CONFIGURATIONS ---
# We use absolute paths to ensure the JSON file lands in the CORRECT folder on your Dell
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
QUOTES_FILE = os.path.join(BASE_DIR, 'quotes.json') # Explicit path

app.config['SECRET_KEY'] = 'dev-key-123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --- INITIALIZE EXTENSIONS ---
db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- CONTEXT PROCESSOR ---
@app.context_processor
def inject_quote():
    local_quotes = [{"content": "Knowledge is power.", "author": "Francis Bacon"}]
    
    # 1. Load the history
    if os.path.exists(QUOTES_FILE):
        try:
            with open(QUOTES_FILE, 'r') as f:
                data = json.load(f)
                if data: local_quotes = data
        except: pass

    # 2. Try to get a NEW one
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=2)
        if response.status_code == 200:
            api_data = response.json()[0]
            new_quote = {"content": api_data['q'], "author": api_data['a']}
            
            # Check if we already have this quote in our JSON
            exists = any(q['content'] == new_quote['content'] for q in local_quotes)
            if not exists:
                local_quotes.append(new_quote)
                with open(QUOTES_FILE, 'w') as f:
                    json.dump(local_quotes[-15:], f, indent=4) # Keep last 15
            
            display_quote = new_quote
        else:
            # If API is busy, SHUFFLE the history so it looks different
            display_quote = random.choice(local_quotes)
    except:
        display_quote = random.choice(local_quotes)
    
    return dict(quote=display_quote)

# --- ROUTES ---

@app.route('/')
def index():
    query = request.args.get('q')
    results = Resource.query.filter(Resource.title.ilike(f'%{query}%')).all() if query else []
    return render_template('index.html', query=query, results=results)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        if User.query.filter_by(email=email).first():
            flash('Email already registered!', 'warning')
            return redirect(url_for('signup'))

        hashed_pw = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256')
        new_user = User(username=request.form.get('username'), email=email, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        db.session.add(Profile(user_id=new_user.id))
        db.session.commit()
        flash('Account created! Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user and check_password_hash(user.password, request.form.get('password')):
            login_user(user)
            return redirect(url_for('profile'))
        flash('Invalid email or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@app.route('/edit_profile', methods=['POST'])
@login_required
def edit_profile():
    profile = Profile.query.filter_by(user_id=current_user.id).first()
    if not profile:
        profile = Profile(user_id=current_user.id)
        db.session.add(profile)
    profile.job_title = request.form.get('job_title')
    profile.hobby = request.form.get('hobby')
    profile.contacts = request.form.get('contacts')
    db.session.commit()
    flash('Profile updated!', 'success')
    return redirect(url_for('profile'))

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    file = request.files.get('file')
    title = request.form.get('title')

    if file and title:
        cover_url = None
        try:
            search_url = f"https://www.googleapis.com/books/v1/volumes?q={title}"
            api_resp = requests.get(search_url, timeout=5)
            if api_resp.status_code == 200:
                data = api_resp.json()
                if 'items' in data:
                    volume_info = data['items'][0].get('volumeInfo', {})
                    cover_url = volume_info.get('imageLinks', {}).get('thumbnail')
        except Exception as e:
            print(f"Metadata API Error: {e}")

        # filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
 
          # Inside upload_file route:
        original_filename = secure_filename(file.filename)
# Create a unique name: "uuid_notes.pdf"
        filename = f"{uuid.uuid4().hex}_{original_filename}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        

        new_res = Resource(
            title=title, 
            description=request.form.get('description'), 
            filename=filename, 
            cover_image=cover_url,
            user_id=current_user.id
        )
        db.session.add(new_res)
        db.session.commit()
        flash('Successfully uploaded!', 'success')
    return redirect(url_for('profile'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/api/delete/<int:resource_id>', methods=['POST'], strict_slashes=False)
@login_required
def delete_resource(resource_id):
    resource = Resource.query.get_or_404(resource_id)
    
    # Check ownership
    if resource.user_id != current_user.id:
        return jsonify({"success": False, "error": "Unauthorized"}), 403

    # Delete physical file
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], resource.filename)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file: {e}")

    # Delete database record
    db.session.delete(resource)
    db.session.commit()
    
    return jsonify({"success": True})

# --- START THE APP ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Ensure upload folder exists
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
        
        # Ensure quotes.json exists with at least one quote so it shows up immediately
        if not os.path.exists(QUOTES_FILE):
            with open(QUOTES_FILE, 'w') as f:
                json.dump([{"content": "Success is a journey.", "author": "Unknown"}], f)
            
    app.run(debug=True)