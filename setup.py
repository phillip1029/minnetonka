"""setup.py: setuptools setup for minnetonka"""

import os
from setuptools import setup 


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name="minnetonka",
	version=minnetonka.__version__,
	packages=['minnetonka', 'minnetonka.test'],
	description="A Python package for business modeling and simulation",
	long_description=read('README'),
    author='David Bridgeland',
    author_email='dave@hangingsteel.com',
    python_requires='>=3.6',
    install_requires=[
        'numpy>=1.15.2',
        'scipy>=1.1.0'
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache License, Version 2.0 (Apache-2.0)'
        ]
	)