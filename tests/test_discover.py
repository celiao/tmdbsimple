# -*- coding: utf-8 -*-

"""
test_discover.py
~~~~~~~~~~~~~~~~

This test suite checks the methods of the Discover class of tmdbsimple.

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
DISCOVER_YEAR = 2004
DISCOVER_VOTE_AVERAGE_GTE = 5


class DiscoverTestCase(unittest.TestCase):
    def test_discover_movie(self):
        discover = tmdb.Discover()
        response = discover.movie(page=1, year=DISCOVER_YEAR)
        self.assertTrue(hasattr(discover, 'results'))

    def test_discover_tv(self):
        discover = tmdb.Discover()
        kwargs = {'page':2, 'vote_average.gte': DISCOVER_VOTE_AVERAGE_GTE}
        response = discover.tv(**kwargs)
        self.assertTrue(hasattr(discover, 'results'))

