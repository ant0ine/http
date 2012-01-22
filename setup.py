from setuptools import setup
from os.path import join, dirname

setup(
    name='http',
    version='0.1.0',
    description='a HTTP library for Python',
    author='Franck Cuny',
    author_email='franck.cuny@gmail.com',
    packages=['http'],
    provides=['http'],
    requires=['fluffyurl', 'urllib3', 'coverage', 'nose', 'unittest2', 'pep8'],
)