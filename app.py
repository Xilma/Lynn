#import the Flask class
from flask import Flask, render_template, redirect, url_for, request, jsonify
import os
import dialogflow
import requests
import json
import pusher


#create an instance of Flask class
app = Flask(__name__)

#Rendering the login page
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

#rendering the signup page
@app.route('/signup')
def signup():
    return render_template('signup.html')

#rendering the chat bot page
@app.route('/lynn', methods=['GET', 'POST'])
def lynn():
    return render_template('lynn.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
    response_text = { "message":  fulfillment_text }
    return jsonify(response_text)

#Function to send a user's message to Dialogflow
def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    if text:
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.fulfillment_text
    except InvalidArgument:
        raise

if __name__ == '__main__':
    app.run(debug=True)

