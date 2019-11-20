from flask import Flask, request, render_template
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/')
def home():
	return render_template('template.html')

@app.route('/l')
def signin():
	return render_template('Login_student.html')

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80)
    app.run(host='0.0.0.0', port=5000)