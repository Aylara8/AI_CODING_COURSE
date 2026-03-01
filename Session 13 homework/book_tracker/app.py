from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import data_manager
import uuid

app = Flask(__name__)
app.secret_key = "secret_reading_key"

@app.route('/')
def index():
    books = data_manager.load_books()
    stats = data_manager.get_stats(books)
    filter_status = request.args.get('status')
    
    if filter_status:
        books = [b for b in books if b['status'] == filter_status]
        
    return render_template('index.html', books=books, stats=stats)

@app.route('/add', methods=['POST'])
def add_book():
    books = data_manager.load_books()
    new_book = {
        "id": str(uuid.uuid4()),
        "title": request.form.get('title'),
        "author": request.form.get('author'),
        "status": request.form.get('status'),
        "rating": request.form.get('rating', 0)
    }
    
    errors = data_manager.validate_book(new_book)
    if errors:
        for error in errors: flash(error, "danger")
        return redirect(url_for('index'))

    books.append(new_book)
    data_manager.save_books(books)
    flash("Book added successfully!", "success")
    return redirect(url_for('index'))

@app.route('/delete/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    # This is the AJAX endpoint
    books = data_manager.load_books()
    books = [b for b in books if b['id'] != book_id]
    data_manager.save_books(books)
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True)