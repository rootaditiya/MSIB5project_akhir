import jwt
from flask import request, render_template, jsonify
import Controller.secretkey as secretkey
# import is_dokter
import Controller.connection as connect
SECRET_KEY = secretkey.SECRET_KEY

db = connect.connection()

def valid(): 
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        user = db.users.find_one({"username": payload['id']})
        return user
    except jwt.ExpiredSignatureError:
        return "expired"
    except jwt.exceptions.DecodeError:
        return "fail"
