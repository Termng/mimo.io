from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/about')
def about():
    return render_template("about.html", text = "Hi Torah, this is a string expected to show like a react prop")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p> Logout </p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return render_template("sign_up.html")
