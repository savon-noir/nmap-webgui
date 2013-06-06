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
