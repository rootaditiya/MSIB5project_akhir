from flask import Flask, render_template, redirect, url_for, request
import Controller.Home.home as dashboard
import Controller.LoginSignup.login_or_signup as auth

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.config['UPLOAD_FOLDER'] = './static/profile_pics'

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

@app.route('/about', methods=['GET'])
def about():
   return render_template('about.html')

@app.route('/report', methods=['GET'])
def report():
   return render_template('report.html')

@app.route('/signin', methods=['GET'])
def login():
   msg = request.args.get("msg")
   return render_template("signin.html", msg=msg)

@app.route("/sign_in", methods=["POST"])
def sign_in():
   return auth.sign_in()

@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
   return auth.check_dup()

@app.route("/sign_up/save", methods=["POST"])
def sign_up():
   return auth.sign_up()


@app.route('/v2', methods=['GET'])
def main():
   main = dashboard.home()
   if main == "success":
      return render_template("home.html")
   elif main == "expired":
      return redirect(url_for("login", msg="Your token has expired"))
   else:
      return redirect(url_for("login", msg="There was problem logging you in"))

@app.route('/v2/konseling', methods=['GET'])
def konseling():
   return render_template('konseling.html')



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)