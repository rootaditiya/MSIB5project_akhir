from flask import render_template, request, redirect, url_for
import jwt
import hashlib
from Controller import connection, secretkey

SECRET_KEY = secretkey.SECRET_KEY
db = connection.connection()

def main():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=["HS256"])
        user_info = db.users.find_one({'username': payload.get('id')})

        return render_template("dokter/articles.html", user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="Your token has expired"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="There was problem logging you in"))
