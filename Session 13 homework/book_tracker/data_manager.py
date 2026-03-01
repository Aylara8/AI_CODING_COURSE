import json
import os

DATA_FILE = 'data/books.json'

def ensure_data_folder():
    """Best Practice: Ensure the data directory exists before saving"""
    os.makedirs('data', exist_ok=True)

def load_books():
    # If the file doesn't exist, return an empty list
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_books(books):
    # Fix: Ensure the folder exists before attempting to write the file
    ensure_data_folder()
    with open(DATA_FILE, 'w') as f:
        json.dump(books, f, indent=4)

def validate_book(data):
    """Server-side validation"""
    errors = []
    if not data.get('title') or len(data['title']) < 2:
        errors.append("Title must be at least 2 characters.")
    if not data.get('author'):
        errors.append("Author is required.")
    return errors if errors else None

def get_stats(books):
    return {
        "total": len(books),
        "finished": len([b for b in books if b['status'] == 'Finished']),
        "reading": len([b for b in books if b['status'] == 'Reading'])
    }