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

        return render_template('pasien/konsul.html', user_info= user_info, status=status)

    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("main"))