import Controller.connection as connect
import Controller.secretkey as secretkey
from flask import render_template, request, jsonify
import hashlib
from datetime import datetime, timedelta
import jwt

db = connect.connection()

SECRET_KEY = secretkey.SECRET_KEY

def sign_in():
    # Sign in
    username_receive = request.form["username_give"]
    password_receive = request.form["password_give"]
    pw_hash = hashlib.sha256(password_receive.encode("utf-8")).hexdigest()
    result = db.users.find_one(
        {
            "username": username_receive,
            "password": pw_hash,
        }
    )
    if result:
        payload = {
            "id": username_receive,
            # the token will be valid for 24 hours
            "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 24),
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        return jsonify(
            {
                "result": "success",
                "token": token,
            }
        )
    # Let's also handle the case where the id and
    # password combination cannot be found
    else:
        return jsonify(
            {
                "result": "fail",
                "msg": "We could not find a user with that id/password combination",
            }
        )

def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    email_receive = request.form['email_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,                               # id
        "password": password_hash,                                  # password
        "profile_name": username_receive,
        "email": email_receive,                          # user's name is set to their id by default
        "role": "pasien",                                          # a profile description
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})

def check_dup():
    # ID we should check whether or not the id is already taken
    print(db)
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({
        'result': 'success',
        'exists': exists
        })
