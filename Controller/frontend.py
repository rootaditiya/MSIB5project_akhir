from flask import render_template, request, jsonify
from Controller import connection
from Controller import auth

db = connection.connection()



def index():
	user_info = auth.main()
	return render_template('index.html', user_info=user_info)
def article():
	user_info = auth.main()
	return render_template('article.html', user_info=user_info)

def about():
	user_info = auth.main()
	return render_template('about.html', user_info=user_info)

def report():
	user_info = auth.main()
	return render_template('report.html', user_info=user_info)

def login():
	msg = request.args.get("msg")
	return render_template('login.html', msg = msg, login=login)

def get_article_new(limit):
	posts = list(db.articles.find({}).sort('date', -1).limit(limit))
	for post in posts:
		post['_id'] = str(post['_id'])
	return jsonify({
		'result':'success',
		'msg': 'Fetch all posts',
		'posts': posts,
	})

def get_article_trend():
	posts = list(db.articles.find({}).sort('visited', -1).limit(4))
	for post in posts:
		post['_id'] = str(post['_id'])

	return jsonify({
		'result':'success',
		'msg': 'Fetch all posts',
		'posts': posts,
	})
