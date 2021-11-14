# -*- coding: utf-8 -*-

# See http://pythonhosted.org/an_example_pypi_project/setuptools.html
# See https://packaging.python.org/tutorials/packaging-projects/#uploading-your-project-to-pypi

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tmdbsimple',
    version='2.8.0',
    author='Celia Oakley',
    author_email='celia.oakley@alumni.stanford.edu',
    description='A Python wrapper for The Movie Database API v3',
    keywords=['movie', 'the movie database', 'movie database', 'tmdb',
                'wrapper', 'database', 'themoviedb', 'moviedb', 'api'],
    url='https://github.com/celiao/tmdbsimple',
    download_url='https://github.com/celiao/tmdbsimple/tarball/2.8.0',
    packages=['tmdbsimple'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['requests'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
    ],
)
