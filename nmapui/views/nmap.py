from nmapui import app
from nmapui.models import NmapTask
from nmapui.tasks import celery_nmap_scan
from flask import Blueprint, render_template, request, redirect, url_for
from flask.ext.login import login_required, current_user

appmodule = Blueprint('nmap', __name__, url_prefix='/nmap')

@appmodule.route('/')
@login_required
def nmap_index():
    return render_template('nmap_index.html')


@appmodule.route('/scan')
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
        NmapTask.add(user_id=current_user.id, task_id=_celery_task.id)
        return redirect(url_for('nmap.nmap_tasks'))

    _nmap_tasks = NmapTask.find(user_id=current_user.id)
    return render_template('nmap_tasks.html', tasks=_nmap_tasks)


@appmodule.route('/report/<report_id>')
@login_required
def nmap_report(report_id):
    _report = None
    if report_id is not None:
        _report = NmapTask.get_report(task_id=report_id)
    return render_template('nmap_report.html', report=_report)


@appmodule.route('/compare')
@login_required
def nmap_compare():
    return render_template('nmap_compare.html')


@appmodule.route('/test', methods=['GET', 'POST'])
#@login_required
def test():
    username = "{0}:{1} {2}".format(current_user.id, current_user.username, type(unicode(current_user.id)))
#    if request.method == 'POST':
#        username = request.args.get('username')
    return render_template('test.html', username=username)
