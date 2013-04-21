__author__ = 'Ronald Bister'
__credits__ = [ 'Ronald Bister' ]
__maintainer__ = 'Ronald Bister'
__email__ =  'mini.pelle@gmail.com'
__license__ = 'CC-BY'
__version__ = '0.1'

from flask import Flask

app = Flask(__name__)
from nmapd import views, config, model
