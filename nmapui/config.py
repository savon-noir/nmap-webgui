import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'nmapd.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'migrations')

CSRF_ENABLED = True
SECRET_KEY = '973fb5503d479a2ccd1ce8b4227bdd3c'
UPLOAD_FOLDER = '/root/python-nmap-daemon/nmapd/nmapp/reports/'

ROLE_USER = 2
ROLE_ADMIN = 4
