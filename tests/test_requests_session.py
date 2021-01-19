# -*- coding: utf-8 -*-
"""
test_requests_session.py
~~~~~~~~~~~~~~

This test suite checks having a user-defined REQUESTS_SESSION with tmdbsimple.

Created by Celia Oakley on 2021-01-18

:copyright: (c) 2021 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

import requests
import unittest
import tmdbsimple as tmdb

from tests import API_KEY, SESSION_ID
tmdb.API_KEY = API_KEY
tmdb.REQUESTS_SESSION = requests.Session()    # specify an explicit session

"""
Constants
"""
MOVIE_ID = 103332
MOVIE_TITLE = 'Ruby Sparks'


class RequestsSessionTestCase(unittest.TestCase):
    def test_requests_session(self):
        id = MOVIE_ID
        title = MOVIE_TITLE
        movie = tmdb.Movies(id)
        movie.info()
        self.assertEqual(movie.title, title)
