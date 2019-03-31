#import the Flask class
from flask import Flask

#create an instance of Flask class
app = Flask(__name__)

@app.route('/')
#function that displays 'Hello World'
def hello_world():
    return 'Hello, World!'
