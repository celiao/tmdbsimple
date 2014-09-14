# -*- coding: utf-8 -*-

"""
test_search.py
~~~~~~~~~~~~~~

This test suite checks the methods of the Search class of tmdbsimple.

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
QUERY_1 = 'Club'
QUERY_2 = 'Avenger'
QUERY_3 = 'Breaking'
QUERY_4 = 'Brad Pitt'
QUERY_5 = 'Oscars'
QUERY_6 = 'Sony Pictures'
QUERY_7 = 'fight'
QUERY_8 = 'blackjack'

class SearchTestCase(unittest.TestCase):
    def test_search_movies(self):
        query = QUERY_1
        search = tmdb.Search()
        response = search.movie(query=query)
        self.assertTrue(hasattr(search, 'results'))

    def test_search_collection(self):
        query = QUERY_2
        search = tmdb.Search()
        response = search.collection(query=query)
        self.assertTrue(hasattr(search, 'results'))

    def test_search_tv(self):
        query = QUERY_3
        search = tmdb.Search()
        response = search.tv(query=query)
        self.assertTrue(hasattr(search, 'results'))

    def test_search_person(self):
        query = QUERY_4
        search = tmdb.Search()
        response = search.person(query=query)
        self.assertTrue(hasattr(search, 'results'))

    def test_search_list(self):
        query = QUERY_5
        search = tmdb.Search()
        response = search.list(query=query)
        self.assertTrue(hasattr(search, 'results'))

    def test_search_company(self):
        query = QUERY_6
        search = tmdb.Search()
        response = search.company(query=query)
        self.assertTrue(hasattr(search, 'results'))

    def test_search_keyword(self):
        query = QUERY_7
        search = tmdb.Search()
        response = search.keyword(query=query)
        self.assertTrue(hasattr(search, 'results'))

    def test_search_multi(self):
        query = QUERY_8
        search = tmdb.Search()
        response = search.multi(query=query)
        self.assertTrue(hasattr(search, 'results'))
