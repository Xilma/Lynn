#import the Flask class
from flask import Flask, render_template

#create an instance of Flask class
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

if __name__ == '__main__':
	app.run(debug=True)
