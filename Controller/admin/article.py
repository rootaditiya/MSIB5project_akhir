import Controller.connection as connect
import Controller.Home.home as valid
from datetime import datetime
from flask import request, jsonify

db = connect.connection()

def save_post(user):
    postime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    title_receive = request.form.get('title_give')
    content_receive = request.form.get('content_give')
    user = request.form.get('usernaame')

    file = request.files['file_give']
    extension = file.filename.split('.')[-1]
    filename = f'static/pic/articles/file_{postime}.{extension}'
    file.save(filename)

    doc = {
        'username':user,
        'file': filename,
        'title': title_receive,
        'content': content_receive,
        'time': datetime.now(),
    }
    db.articles.insert_one(doc)
    return jsonify({
         'message':'Data was saved'
        })


def show_post(user):
    articles = list(db.diary.find({'username': user},{}).sort('time', -1))
    return jsonify({'articles': articles})
