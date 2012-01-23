from setuptools import setup
from os.path import join, dirname

setup(
    name='http',
    version='0.1.0',
    description='HTTP library for Python',
    long_description=open('README').read(),
    author='Franck Cuny',
    author_email='franck.cuny@gmail.com',
    url='https://github.com/franckcuny/http',
    packages=['http'],
    license='MIT',
    requires=['coverage', 'nose', 'unittest2', 'pep8'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
    ]
)