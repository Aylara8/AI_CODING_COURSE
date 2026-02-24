from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/jinja')
def about():
    username = "Aylar"
    food = ["Plow"]
    
    return render_template('jinja.html', username=username, items=items)

if __name__ == '__main__':
    app.run(debug=True)






# now i created templates folder with index html in it of my portfolio,
#  then i created static folder with css and js files in it of my portfolio ,
#  I created app.py and which code i need to write there for opening my portflio
