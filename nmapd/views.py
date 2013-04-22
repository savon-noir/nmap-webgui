import os
from nmapd import app, login_manager, nmap_manager
from nmapd import models
from flask import render_template, request, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from werkzeug import secure_filename


@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('login'))


@app.route('/nmap/')
@login_required
def nmap_index():
    return render_template('nmap_index.html')


@app.route('/nmap/scans/')
@login_required
def nmap_scan():
    return render_template('nmap_scans.html')


@app.route('/nmap/reports/')
@login_required
def nmap_reports():
    reports = []
    reports = nmap_manager.get_reports()
    msg = ''
    #    msg = "Error while trying to connect to data store"
    return render_template('nmap_reports.html', msg=msg, reports=reports)


@app.route('/nmap/compare/')
@login_required
def nmap_compare():
    return render_template('nmap_compare.html')


@app.route('/test/', methods=['GET', 'POST'])
#@login_required
def test():
    username = 'blanked'
    if request.method == 'POST':
        username = request.args.get('username')
    return render_template('test.html', username=username)


@app.route('/nmap/report_upload/', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('nmap_reports'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@login_manager.user_loader
def load_user(userid):
    return models.User.query.get(int(userid))


@app.route("/login", methods=["GET", "POST"])
def login():
    if (request.method == 'POST' and 'username' in request.form and
       'password' in request.form):
        username = request.form['username']
        password = request.form['password']
        app_user = models.User.query.filter_by(username=username).first()
        if app_user and app_user.credentials_valid(password):
            login_user(app_user)
            return redirect(request.args.get("next") or url_for("nmap_index"))
        else:
            flash("login failed: check username and password")
    return render_template("nmap_login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
