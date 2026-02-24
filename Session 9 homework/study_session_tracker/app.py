from flask import Flask, render_template, request, redirect, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'sessions.json'

# Helper to read/write JSON
def load_data():
    if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def home():
    # Requirement: Traditional Route (Home)
    sessions = load_data()
    return render_template('index.html', sessions=sessions)

@app.route('/add', methods=['POST'])
def add_item():
    # Requirement: Traditional Form Route
    try:
        subject = request.form.get('subject')
        duration = int(request.form.get('duration'))
        date = request.form.get('date')
        
        sessions = load_data()
        new_session = {
            "id": len(sessions) + 1 if sessions else 1,
            "subject": subject,
            "duration": duration,
            "date": date
        }
        sessions.append(new_session)
        save_data(sessions)
        return redirect('/')
    except Exception as e:
        return f"Error adding session: {e}", 400

@app.route('/api/items')
def get_items():
    # Requirement: API Route returning JSON
    return jsonify({'items': load_data()})

@app.route('/api/delete/<int:id>', methods=['DELETE'])
def delete_item(id):
    # Requirement: API Delete Route
    sessions = load_data()
    initial_count = len(sessions)
    sessions = [s for s in sessions if s['id'] != id]
    
    if len(sessions) < initial_count:
        save_data(sessions)
        return jsonify({'success': True, 'message': 'Deleted successfully'})
    return jsonify({'success': False, 'message': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)