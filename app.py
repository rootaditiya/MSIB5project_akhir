from flask import Flask
from Controller import frontend, auth, backend
from Controller.dokter import article_user

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

## Setiap URL memiliki nama fungsi yang sama,
## Alama-alamat pada route('/'), dll. harus tidak boleh sama.

@app.route('/', methods=['GET'])
def index():
   return frontend.index()

@app.route('/articles', methods=['GET'])
def article():
   return frontend.article()

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

@app.route("/v2/<user>/articles")
def user_article(user):
   return article_user.main()

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)