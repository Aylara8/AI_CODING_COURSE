import json
import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey" # Needed for flashing error messages
DATA_FILE = 'recipes.json'

def load_recipes():
    """Load recipes from the JSON file with error handling."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_recipes(recipes):
    """Save the list of recipes to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(recipes, f, indent=4)

@app.route('/')
def index():
    query = request.args.get('search', '').lower()
    recipes = load_recipes()
    
    # Filter functionality
    if query:
        recipes = [r for r in recipes if query in r['name'].lower()]
        
    return render_template('index.html', recipes=recipes, count=len(recipes), query=query)

@app.route('/add', methods=['POST'])
def add_recipe():
    name = request.form.get('name')
    ingredients = request.form.get('ingredients')
    instructions = request.form.get('instructions')

    # Basic error handling for empty inputs
    if not name or not ingredients or not instructions:
        flash("All fields are required!")
        return redirect(url_for('index'))

    recipes = load_recipes()
    recipes.append({
        'name': name,
        'ingredients': ingredients,
        'instructions': instructions
    })
    save_recipes(recipes)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_recipe(index):
    recipes = load_recipes()
    if 0 <= index < len(recipes):
        recipes.pop(index)
        save_recipes(recipes)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)