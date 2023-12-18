from flask import render_template, request

def index():
	return render_template('index.html')
def article():
	return render_template('article.html')

def about():
	return render_template('about.html')

def report():
	return render_template('report.html')

def login():
	msg = request.args.get("msg")
	return render_template('login.html', msg = msg)
