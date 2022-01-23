# -*- coding: utf-8 -*-

"""
test_discover.py
~~~~~~~~~~~~~~~~

This test suite checks the methods of the Discover class of tmdbsimple.

Created by Celia Oakley on 2013-11-05

:copyright: (c) 2013-2022 by Celia Oakley.
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
DISCOVER_VOTE_AVERAGE_LTE = 5


class DiscoverTestCase(unittest.TestCase):
    def test_discover_movie(self):
        discover = tmdb.Discover()
        discover.movie(page=1, year=DISCOVER_YEAR)
        self.assertTrue(hasattr(discover, 'results'))

    # Test dot usage
    def test_discover_movie_dot_gte(self):
        discover = tmdb.Discover()
        kwargs = {'page': 2, 'vote_average.gte': DISCOVER_VOTE_AVERAGE_GTE}
        discover.movie(**kwargs)
        self.assertTrue(hasattr(discover, 'results'))

    # Test underscore usage
    def test_discover_movie_underscore_gte(self):
        discover = tmdb.Discover()
        discover.movie(page=2, vote_average_gte=DISCOVER_VOTE_AVERAGE_GTE)
        self.assertTrue(hasattr(discover, 'results'))

    def test_discover_movie_underscore_lte(self):
        discover = tmdb.Discover()
        discover.movie(page=2, vote_average_lte=DISCOVER_VOTE_AVERAGE_LTE)
        self.assertTrue(hasattr(discover, 'results'))

    def test_discover_tv_underscore_gte(self):
        discover = tmdb.Discover()
        discover.tv(page=2, vote_average_gte=DISCOVER_VOTE_AVERAGE_GTE)
        self.assertTrue(hasattr(discover, 'results'))

    def test_discover_tv_underscore_lte(self):
        discover = tmdb.Discover()
        discover.tv(page=2, vote_average_lte=DISCOVER_VOTE_AVERAGE_LTE)
        self.assertTrue(hasattr(discover, 'results'))
