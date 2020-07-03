# -*- coding: utf-8 -*-

"""
keys.py
~~~~~~~

This file contains the private keys for tmdbsimple.

See: http://docs.themoviedb.apiary.io
     http://docs.themoviedb.apiary.io/#accounts
     http://docs.themoviedb.apiary.io/#authentication
     https://www.themoviedb.org/documentation/api/sessions
"""

import os

API_KEY = os.environ.get('TMDB_API_KEY') or '<YOUR TMDB API_KEY HERE>'
USERNAME = os.environ.get('TMDB_USERNAME') or '<YOUR TMDB USERNAME HERE>'
PASSWORD = os.environ.get('TMDB_PASSWORD') or '<YOUR TMDB PASSWORD HERE>'
SESSION_ID = os.environ.get('TMDB_SESSION_ID') or '<YOUR TMDB SESSION_ID HERE>'
