__author__ = 'Ronald Bister'
__email__ =  'mini.pelle@gmail.com'
__license__ = 'CC-BY'
__version__ = '0.1'

from flask import Flask
from nmapui import config
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object(config)

mongo = PyMongo(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from nmapui import views

if __name__ == '__main__':
    app.run()
