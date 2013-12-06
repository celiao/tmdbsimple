# See http://pythonhosted.org/an_example_pypi_project/setuptools.html

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'tmdbsimple',
    version = '0.2',
    author = 'Celia Oakley',
    author_email = 'celia.oakley@alumni.stanford.edu',
    description = 'A Python wrapper for The Movie Database API v3',
    keywords = ['movie', 'the movie database', 'movie database', 'tmdb', 'wrapper'],
    url = 'https://github.com/celiao/tmdbsimple',   # URL to github repo
    download_url = 'https://github.com/celiao/tmdbsimple/tarball/0.2',
    packages = ['tmdbsimple'],
    long_description=read('README.rst'),
    install_requires = ['requests>=0.11.1'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
)
