__author__ = 'Ronald Bister'
__credits__ = [ 'Ronald Bister' ]
__maintainer__ = 'Ronald Bister'
__email__ =  'mini.pelle@gmail.com'
__license__ = 'CC-BY'
__version__ = '0.1'

from flask import Flask
from nmapui import config
from nmapui.manager import NmapManager
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

db = SQLAlchemy(app)

nmap_manager = NmapManager()
from nmapui import views, manager
