from distutils.core import setup

setup(
    name='nmapd',
    version='0.0.1',
    author='Ronald Bister',
    author_email='mini.pelle@gmail.com',
    packages=['nmapd', 'nmapd.test'],
    url='http://pypi.python.org/pypi/nmapd/',
    license='LICENSE.txt',
    description='A small web application to enable you to run nmap scans, parse and compare the results in your browser or via its Restful API',
    long_description=open('README').read(),
)
