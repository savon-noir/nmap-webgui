import os
from nmapd import app
from nmapd.model import NmapManager
from flask import render_template, request, redirect
from werkzeug import secure_filename

nmap_manager = NmapManager()
app.config['UPLOAD_FOLDER'] = nmap_manager.upload_folder


@app.route('/', methods=['GET', 'POST'])
def index(self):
    return 'Nmap web service'


@app.route('/nmap/')
def nmap_index():
    return render_template('nmap_index.html')


@app.route('/nmap/scans/')
def nmap_scan():
    return render_template('nmap_scans.html')


@app.route('/nmap/reports/')
def nmap_reports():
    rlist = nmap_manager.get_reports()
    return render_template('nmap_reports.html', reports=rlist)


@app.route('/nmap/compare/')
def nmap_compare():
    return render_template('nmap_compare.html')


@app.route('/test/')
def html_test():
    return render_template('test.html')


@app.route('/nmap/report_upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/nmap/reports/')
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
