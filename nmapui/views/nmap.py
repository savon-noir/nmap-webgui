from nmapui import app
from nmapui.models import Reports
from nmapui.tasks import celery_nmap_scan
from flask import Blueprint, render_template, request, redirect, url_for
from flask.ext.login import login_required, current_user

appmodule = Blueprint('nmap', __name__, url_prefix='/nmap')

@appmodule.route('/')
@login_required
def nmap_index():
    return render_template('nmap_index.html')


@appmodule.route('/scans/')
@login_required
def nmap_scan():
    return render_template('nmap_scans.html')


@appmodule.route('/tasks', methods=['GET', 'POST'])
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
        return redirect(url_for('nmap.nmap_reports'))
    return render_template('nmap_tasks.html')


@appmodule.route('/reports/')
@login_required
def nmap_reports():
    reports = Reports.find(user_id=current_user.id)
    msg = 'Dumping reports'
    #    msg = "Error while trying to connect to data store"
    return render_template('nmap_reports.html', msg=msg, reports=reports)


@appmodule.route('/compare/')
@login_required
def nmap_compare():
    return render_template('nmap_compare.html')


@appmodule.route('/test/', methods=['GET', 'POST'])
#@login_required
def test():
    username = "{0}:{1} {2}".format(current_user.id, current_user.username, type(unicode(current_user.id)))
#    if request.method == 'POST':
#        username = request.args.get('username')
    return render_template('test.html', username=username)
