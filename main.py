from flask import Flask, request, render_template
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/')
def home():
	return render_template('template.html')



