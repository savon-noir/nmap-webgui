# nmap-webgui

## Code status

This webapp is being developped. Basic structure is here, you can launch scan and have nmap scan reports automatically stored but no more so far :p

## Use cases
nmap-webgui is a multi-user small web application based on flask to enable the user to:

- launch nmap scans (DONE)
- schedule periodic scans
- review scan reports
- diff and compare scan reports
- display stats of scan reports

nmap-webgui is relying on the following technologies:

- flask
- celery
- rabbitmq
- mongodb
- python-libnmap

## Dependencies

Following packages need to be installed:

- flask via pip
- flask-login via pip
- flask-pymongo via pip
- flask-scripts via pip (optional)
- rabbitmq server (no specific config needed)
- mongodb daemon (to store users data and celery tasks)

##Quick install

This is a draft on how to install and run nmap-webgui:

```bash
    # install packages in a virtualenv or whatever
    $ pip install Flask
    $ pip install Flask-Login
    $ pip install Flask-PyMongo
    $ pip install celery

    # install mongodb and rabbitmq
    $ yum install mongod
    $ yum install mongod-server
    $ yum install rabbitmq-server

    # start rabbitmq and mongodb
    $ service mongod start
    $ service rabbitmq-server start

    # install the webgui
    $ git clone https://savon_noir@bitbucket.org/savon_noir/nmap-webgui.git
    $ cd nmap-webgui
    $ python setup.py install

    # run celery
    $ celery -A nmapui.tasks worker --loglevel=debug

    # add a user, start the web app in debug and login
    $ python manage.py adduser <username> <email>
    $ python manage.py runserver
```
