from flask import render_template, request, redirect, url_for, jsonify
import jwt
import hashlib
from Controller import connection, secretkey
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId
import json
from bson import json_util
import os

SECRET_KEY = secretkey.SECRET_KEY
db = connection.connection()

def main():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        status = user_info = db.users.find_one({'username': payload.get('id')})

        return render_template('dokter/articles.html', user_info= user_info, status=status)

    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("main"))

def post():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        user_info = db.users.find_one({'username': payload.get('id')})

        postime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

        title_receive = request.form.get('title_give')
        subtitle_receive = request.form.get('subtitle_give')
        content_receive = request.form.get('content_give')
        date_receive = request.form["date_give"]

        if "file_give" in request.files:
            file = request.files['file_give']
            filename = secure_filename(file.filename)
            extension = file.filename.split('.')[-1]
            filename = f'static/pic/articles/file_{postime}.{extension}'
            file.save(filename)

        doc = {
            "username": user_info['username'],
            "title": title_receive,
            "subtitle": subtitle_receive,
            "file": filename,
            "content": content_receive,
            "date": date_receive,
            "visited": 0,
        }
        db.articles.insert_one(doc)
        
        return jsonify({"result": "success", "msg": "Posting successful!"})


    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("main"))

def get():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        posts = list(db.articles.find({'username': payload.get('id')}).sort('date', -1))
        for post in posts:
            post['_id'] = str(post['_id'])
        return jsonify({
            'result':'success',
            'msg': 'Fetch all posts',
            'posts': posts,
            })
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for('main'))

def get_one(id):
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        post = db.articles.find_one(ObjectId(id))
        post['_id'] = str(post['_id'])

        post = json.loads(json_util.dumps(post))
        return jsonify({
            'result': "success",
            'msg': 'fetch an artcle',
            'post': post,
            })
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for('main'))


def del_article():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({'username': payload.get('id')})
        id = request.form.get('id_give')
        db.articles.delete_one({"_id":ObjectId(id)})
        return jsonify({
            'result':'success',
            'msg': 'delete posts',
        })
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for('main'))

def edit_article():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({'username': payload.get('id')})
        postime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

        id = request.form.get('id_give')
        print(f'id article = {id}')
        article = db.articles.find_one(ObjectId(id))
        print(f'data = {article}')
        file = article['file']

        title_receive = request.form.get('title_give')
        subtitle_receive = request.form.get('subtitle_give')
        content_receive = request.form.get('content_give')
        date_receive = request.form["date_give"]
        doc = {
            "username": user_info['username'],
            "title": title_receive,
            "subtitle": subtitle_receive,
            "content": content_receive,
            "edit-on": date_receive,
            "visited": 0,
        }

        if "file_give" in request.files:
            print(request.files['file_give'])
            os.remove(article['file'])
            file = request.files['file_give']
            filename = secure_filename(file.filename)
            extension = file.filename.split('.')[-1]
            filename = f'static/pic/articles/file_{postime}.{extension}'
            file.save(filename)
            doc["profile_pic"] = filename

        db.articles.update_one({"_id": ObjectId(id)}, {"$set": doc})
        
        return jsonify({
            'result':'success',
            'msg': 'posts was edited!',
        })
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for('main'))
