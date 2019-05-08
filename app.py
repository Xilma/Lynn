#import the Flask class
from flask import Flask, render_template

#create an instance of Flask class
app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/lynn')
def lynn():
    return render_template('lynn.html')

@app.route('/friends')
def friends():
    return render_template('friends.html')

@app.route('/help_center')
def help_center():
    return render_template('helpcenter.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
	app.run(debug=True)
