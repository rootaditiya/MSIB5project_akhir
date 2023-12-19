import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, request
from Controller import frontend, auth, backend
from Controller.dokter import article_user, konseling

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

## Setiap URL memiliki nama fungsi yang sama,
## Alama-alamat pada route('/'), dll. harus tidak boleh sama.

@app.route('/', methods=['GET'])
def index():
   return frontend.index()

@app.route('/get_article_new/', methods=['GET'])
def get_article_new():
   return frontend.get_article_new(100)

@app.route('/get_article_trend/', methods=['GET'])
def get_article_trend():
   return frontend.get_article_trend()

@app.route('/articles', methods=['GET'])
def article():
   return frontend.article()

@app.route('/articles/<judul>', methods=['GET'])
def baca(judul):
   judul = judul
   id = request.args.get('id')
   return frontend.baca(id)

@app.route('/about', methods=['GET'])
def about():
   return frontend.about()

@app.route('/report', methods=['GET'])
def report():
   return frontend.report()

@app.route('/login', methods=['GET'])
def login():
   return frontend.login()

@app.route("/sign_in", methods=["POST"])
def sign_in():
   return auth.sign_in()

@app.route("/sign_up/save", methods=["POST"])
def sign_up():
   return auth.sign_up()

@app.route("/sign_up/check_dup", methods=["POST"])
def check_dup():
   return auth.check_dup()

@app.route("/v2")
def main():
   return backend.main()

@app.route("/v2/<user>/konseling")
def konseling(user):
   user = user
   return f"laman konseling - {user}"

@app.route("/v2/articles")
def user_article():
   return article_user.main()

@app.route("/v2/post-article", methods=["POST"])
def post_article():
   return article_user.post()

@app.route('/v2/get-article', methods=['GET'])
def get_articles():
   return article_user.get()

@app.route('/v2/del-article', methods=['POST'])
def del_articles():
   return article_user.del_article()

@app.route('/v2/get-article/<id>', methods=['GET'])
def get_one_articles(id):
   id = id
   return article_user.get_one(id)

@app.route('/v2/edit-article', methods=['POST'])
def edit_articles():
   return article_user.edit_article()

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)