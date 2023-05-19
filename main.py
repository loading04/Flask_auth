from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# Line below only required once, when creating DB.
# with app.app_context():
#    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(entity=User, ident=user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        new_user = User()

        new_user.name = request.form.get("name")
        new_user.email = request.form.get("email")

        hashed_pwd = generate_password_hash(password=request.form.get("password"), method='pbkdf2:sha256',
                                            salt_length=8)
        print(hashed_pwd)

        new_user.password = hashed_pwd

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('secrets'))
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        get_email = request.form.get('email')
        get_password = request.form.get('password')
        user = db.session.query(User).filter_by(email=get_email).first()
        try:
            if check_password_hash(user.password, get_password):
                login_user(user)
                return redirect(url_for('secrets'))
        except:
            return redirect(url_for('register'))

    return render_template("login.html")


@app.route('/secrets')
def secrets():
    if current_user.is_authenticated:
        name = current_user.name
    else:
        name = None
    return render_template("secrets.html", data=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download:')
def download():
    return send_from_directory(directory='static/files', path="cheat_sheet.pdf", as_attachment=False)


if __name__ == "__main__":
    app.run(debug=True)
