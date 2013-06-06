from nmapui import login_manager
from nmapui.models import Users
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required

appmodule = Blueprint('ui', __name__)

@appmodule.route('/', methods=['GET'])
def index():
    return redirect(url_for('ui.login'))

@login_manager.user_loader
def load_user(user_id):
    return Users.get(user_id)

@appmodule.route("/login", methods=["GET", "POST"])
def login():
    if (request.method == 'POST' and 'username' in request.form and
       'password' in request.form):
        app_user = None
        username = request.form['username']
        password = request.form['password']
        if 'username' in request.form and len(request.form['username']):
            app_users = Users.find(username=username)
            if len(app_users) != 1:
                flash("login failed: check username and password")
                app_user = None
            else:
                app_user = app_users[0]

        if app_user and app_user.credentials_valid(password):
            login_user(app_user)
            return redirect(request.args.get("next") or url_for("nmap.nmap_index"))
    return render_template("nmap_login.html")


@appmodule.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('ui.index'))
