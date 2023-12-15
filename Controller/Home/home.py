import jwt
from flask import request
import Controller.secretkey as secretkey

SECRET_KEY = secretkey.SECRET_KEY

def home(): 
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])

        return "success"
    except jwt.ExpiredSignatureError:
        return "expired"
    except jwt.exceptions.DecodeError:
        return "fail"
