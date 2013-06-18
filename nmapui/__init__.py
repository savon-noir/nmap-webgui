__author__ = 'Ronald Bister'
__email__ =  'mini.pelle@gmail.com'
__license__ = 'CC-BY'
__version__ = '0.1'

from flask import Flask
from nmapui import config
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager
import datetime

app = Flask(__name__)
app.config.from_object(config)

mongo = PyMongo(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "ui.login"

from nmapui.views import ui
from nmapui.views import nmap
app.register_blueprint(ui.appmodule)
app.register_blueprint(nmap.appmodule)

def unix2datetime(unixstr):
    _rstr = ''
    try:
        _dtime = datetime.datetime.fromtimestamp(int(unixstr))
        _rstr = _dtime.strftime('%d/%m/%Y %H:%M:%S')
    except ValueError:
        _rstr = 'Unknown'
    return _rstr

app.jinja_env.filters['unix2datetime'] = unix2datetime

if __name__ == '__main__':
    app.run()
