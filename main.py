from flask import Flask, request, render_template
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


# @app.route('/')
# def template():
# 	return render_template('template.html')

@app.route('/forgetpwEmail')
def forgetpwEmail():
	return render_template('ForgetPwEmail.html')

@app.route('/forgetpwNew')
def forgetpwNew():
	return render_template('ForgetPwNew.html')

@app.route('/forgetpwVer')
def forgetpwVer():
	return render_template('ForgetPwVer.html')

@app.route('/form_advisor')
def form_advisor():
	return render_template('Form_Advicer.html')
    
@app.route('/form')
def form():
	return render_template('Form.html')

@app.route('/form2student')
def form2student():
	return render_template('Form2Student.html')

@app.route('/formboss')
def formboss():
	return render_template('FormBoss.html')

@app.route('/formboss2')
def formboss2():
	return render_template('FormBoss2.html')

@app.route('/formstudent')
def formstudent():
	return render_template('FormStudent.html')

@app.route('/formtc')
def formtc():
	return render_template('FormTC.html')

@app.route('/home_advisor')
def home_advisor():
	return render_template('Home_Advicer.html')

@app.route('/home_advisor2')
def home_advisor2():
	return render_template('Home_Advicer2.html')

@app.route('/home_boss')
def home_boss():
	return render_template('Home_Boss.html')

@app.route('/home_boss2')
def home_boss2():
	return render_template('Home_Boss2.html')

@app.route('/home_tc')
def home_tc():
	return render_template('Home_TC.html')

@app.route('/home_tc2')
def home_tc2():
	return render_template('Home_TC2.html')

@app.route('/home')
def home():
	return render_template('Home.html')

@app.route('/login_advisor')
def login_advisor():
	return render_template('Login_Advicer.html')

@app.route('/login_boss')
def login_boss():
	return render_template('Login_Boss.html')

@app.route('/')
def login_student():
	return render_template('Login_student.html')

@app.route('/login_tc')
def login_tc():
	return render_template('Login_TC.html')

@app.route('/tracking_1')
def tracking_1():
	return render_template('Tracking_1.html')

@app.route('/tracking_2')
def tracking_2():
	return render_template('Tracking_2.html')

@app.route('/tracking_3cancel')
def tracking_3cancel():
	return render_template('Tracking_3cancel.html')

@app.route('/tracking_3none')
def tracking_3none():
	return render_template('Tracking_3none.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    #app.run(host='0.0.0.0', port=5000,debug=True)