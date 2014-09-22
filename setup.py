# -*- coding: utf-8 -*-

# See http://pythonhosted.org/an_example_pypi_project/setuptools.html

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'tmdbsimple',
    version = '1.0.0',
    author = 'Celia Oakley',
    author_email = 'celia.oakley@alumni.stanford.edu',
    description = 'A Python wrapper for The Movie Database API v3',
    keywords = ['movie', 'the movie database', 'movie database', 'tmdb', 
                'wrapper', 'database', 'themoviedb', 'moviedb', 'api'],
    url = 'https://github.com/celiao/tmdbsimple',
    download_url = 'https://github.com/celiao/tmdbsimple/tarball/1.0.0',
    packages = ['tmdbsimple'],
    long_description=read('README.rst'),
    install_requires = ['requests>=2.3.0'],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Utilities",
    ],
)
