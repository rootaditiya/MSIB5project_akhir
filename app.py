from pymongo import MongoClient
import jwt
from datetime import datetime, timedelta
from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = './static/profile_pics'

SECRET_KEY = 'KLP6'

MONGODB_CONNECTION_STRING = ''

## Setiap URL memiliki nama fungsi yang sama,
## Alama-alamat pada route('/'), dll. harus tidak boleh sama.

@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')


@app.route('/articles', methods=['GET'])
def articles():
   return render_template('article.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)