# -*- coding: utf-8 -*-
"""
test_requests_session.py
~~~~~~~~~~~~~~

This test suite checks having a user-defined REQUESTS_SESSION with tmdbsimple.

Created by Celia Oakley on 2022-01-18

:copyright: (c) 2013-2022 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

import unittest
import tmdbsimple as tmdb

from tests import API_KEY
tmdb.API_KEY = API_KEY

import requests
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
