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
            return redirect(url_for('lynn'))
        return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/lynn')
def lynn():
    return render_template('lynn.html')

if __name__ == '__main__':
	app.run(debug=True)
