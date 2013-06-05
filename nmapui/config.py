import os
basedir = os.path.abspath(os.path.dirname(__file__))

MONGO_DBNAME = 'nmapuidb'
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
CSRF_ENABLED = True
SECRET_KEY = '973fb5503d479a2ccd1ce8b4227bdd3c'
UPLOAD_FOLDER = '/root/python-nmap-daemon/nmapd/nmapp/reports/'

ROLE_USER = 2
ROLE_ADMIN = 4
