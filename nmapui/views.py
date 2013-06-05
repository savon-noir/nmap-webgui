import os
from nmapui import app, login_manager, mongo
from nmapui.models import Users, Reports
from nmapui.tasks import celery_nmap_scan
from flask import render_template, request, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, current_user
from werkzeug import secure_filename
from bson.objectid import ObjectId

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


@app.route('/nmap/tasks', methods=['GET', 'POST'])
@login_required
def nmap_tasks():
    scantypes = [ "-sT", "-sT", "-sS", "-sA", "-sW", "-sM",
            "-sN", "-sF", "-sX", "-sU" ]

    if request.method == "POST":
        if 'targets' in request.form:
            targets = request.form["targets"]
        else:
            abort(401)
        options = ""
        scani = int(request.form['scantype']) if 'scantype' in request.form else 0
        if 'ports' in request.form and len(request.form['ports']):
            portlist = "-p " + request.form['ports']
        else:
            portlist = ''
        noping = '-P0' if 'noping' in request.form else ''
        osdetect = "-O" if 'os' in request.form else ''
        bannerdetect = "-sV" if 'banner' in request.form else ''
        options = "{0} {1} {2} {3} {4}".format(scantypes[scani],
                                                  portlist,
                                                  noping,
                                                  osdetect,
                                                  bannerdetect)
        _celery_task = celery_nmap_scan.delay(targets=str(targets),
                                              options=str(options))
        Reports.add(user_id=current_user.id, task_id=_celery_task.id)
        return redirect(url_for('nmap_reports'))
    return render_template('nmap_tasks.html')


@app.route('/nmap/reports/')
@login_required
def nmap_reports():
    reports = Reports.find()
    msg = 'Dumping reports'
    #    msg = "Error while trying to connect to data store"
    return render_template('nmap_reports.html', msg=msg, reports=reports)


@app.route('/nmap/compare/')
@login_required
def nmap_compare():
    return render_template('nmap_compare.html')


@app.route('/test/', methods=['GET', 'POST'])
#@login_required
def test():
    username = "{0}:{1} {2}".format(current_user.id, current_user.username, type(unicode(current_user.id)))
#    if request.method == 'POST':
#        username = request.args.get('username')
    return render_template('test.html', username=username)

@login_manager.user_loader
def load_user(user_id):
    return Users.get(user_id)

@app.route("/login", methods=["GET", "POST"])
def login():
    if (request.method == 'POST' and 'username' in request.form and
       'password' in request.form):
        username = request.form['username']
        password = request.form['password']
        app_users = Users.find(username=username)
        if len(app_users) != 1:
            app_user = None
            flash("login failed: check username and password")
        else:
            app_user = app_users[0]

        if app_user and app_user.credentials_valid(password):
            login_user(app_user)
            return redirect(request.args.get("next") or url_for("nmap_index"))
    return render_template("nmap_login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
