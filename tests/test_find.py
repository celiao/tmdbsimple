# -*- coding: utf-8 -*-

"""
test_find.py
~~~~~~~~~~~~

This test suite checks the methods of the Find class of tmdbsimple.

Created by Celia Oakley on 2013-11-05

:copyright: (c) 2013-2014 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

import unittest
import tmdbsimple as tmdb

from tests import API_KEY
tmdb.API_KEY = API_KEY

"""
Constants
"""
FIND_MOVIE_ID = 'tt0266543'
FIND_SOURCE = 'imdb_id'
FIND_TITLE = 'Finding Nemo'


class FindTestCase(unittest.TestCase):
    def test_find_info(self):
        id = FIND_MOVIE_ID
        external_source = FIND_SOURCE
        title = FIND_TITLE
        find = tmdb.Find(id)
        response = find.info(external_source=external_source)
        self.assertEqual(find.movie_results[0]['title'], title)
