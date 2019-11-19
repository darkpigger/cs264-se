from flask import Flask, request, render_template
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/')
def home():
	return render_template('template.html')

@app.route('/chat')
def chat():
	return render_template('chat.html')

