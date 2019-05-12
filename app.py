#import the Flask class
from flask import Flask, render_template, redirect, url_for, request

#create an instance of Flask class
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
        return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/lynn')
def lynn():
    return render_template('lynn.html')

@app.route('/lynn/chat')
def chatbot():
    return render_template('chatbot.html')

@app.route('/friends')
def friends():
    return render_template('friends.html')

@app.route('/helpcenter')
def help_center():
    return render_template('helpcenter.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
	app.run(debug=True)
