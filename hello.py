from flask import Flask

app = Flask(__name__)

# make the route
@app.route('/')

# now define a function
def hello():
    return render_template('home.html')

# make a second route
@app.route('/about')

# now make a function that goes with about
def preds():
    return render_template('about.html')