from nmapp.views import *
#from flask import Flask, render_template
#app = Flask(__name__)
#
#@app.route('/', methods=['GET', 'POST'])
#def index():
#    return 'Nmap web service'
#
#@app.route('/nmap/')
#def nmap_index():
#    #rlist = list_reports(username)
#    return render_template('nmap_index.html')
#
#@app.route('/nmap/scans/')
#def nmap_scan():
#    return render_template('nmap_scans.html')
#
#@app.route('/nmap/reports/')
#def nmap_reports():
#    return render_template('nmap_reports.html')
#
#@app.route('/nmap/compare/')
#def nmap_compare():
#    return render_template('nmap_compare.html')
#
#@app.route('/test/')
#def html_test():
#    return render_template('test.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
