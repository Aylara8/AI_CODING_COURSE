from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Passing a simple variable
    name = "Aylar" 
    return render_template('home.html', name=name)

@app.route('/about')
def about():
    # Passing a string for a bio
    bio = "I am a student and I have a passion for learning new programming languages and exploring different technologies."
    return render_template('about.html', bio=bio)

@app.route('/hobbies')
def hobbies():
    # Passing a list to demonstrate iteration in templates
    my_hobbies = ["Piano", "Languages", "Drawing", "Coding", "Reading"]
    return render_template('hobbies.html', hobbies=my_hobbies)

if __name__ == '__main__':
    app.run(debug=True)