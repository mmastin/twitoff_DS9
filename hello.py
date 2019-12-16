from flask import Flask

app = Flask(__name__)

# make the route
@app.route('/')

# now define a function
def hello():
    return 'Hello World!'