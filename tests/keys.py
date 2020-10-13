# -*- coding: utf-8 -*-

"""
keys.py
~~~~~~~

This file contains the private keys for tmdbsimple.

See:
    https://developers.themoviedb.org/3/getting-started/introduction
    https://developers.themoviedb.org/3/getting-started/authentication
    https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id
"""

import os

API_KEY = os.environ.get('TMDB_API_KEY') or '<YOUR TMDB API_KEY HERE>'
USERNAME = os.environ.get('TMDB_USERNAME') or '<YOUR TMDB USERNAME HERE>'
PASSWORD = os.environ.get('TMDB_PASSWORD') or '<YOUR TMDB PASSWORD HERE>'
SESSION_ID = os.environ.get('TMDB_SESSION_ID') or '<YOUR TMDB SESSION_ID HERE>'
