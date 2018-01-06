# -*- coding: utf-8 -*-

"""
test_base.py
~~~~~~~~~~~~~~~

This test suite checks the methods of the TMDB class of tmdbsimple.

Created by Celia Oakley on 2018-01-06

:copyright: (c) 2018 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

import unittest
import tmdbsimple as tmdb

from tests import API_KEY, USERNAME, PASSWORD
tmdb.API_KEY = API_KEY

"""
Constants
"""
MOVIE_ID = 103332
MOVIEQUERY1 = 'Matrix'
MOVIEQUERY2 = 'Star Wars'

class TMDBTestCase(unittest.TestCase):
    # We want to be able to call methods multiple times.
    # If a method returns a dict with a key of the same name as the method,
    # e.g., Movies.keywords(), an attribute won't be set.
    # Confirm for this case that the method can be called again.
    def test_tmdb_set_attrs_to_values_method_equals_attribute(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        response = movie.keywords()
        raised = False
        try:
            movie.keywords()
        except:
            raised = True
        self.assertFalse(raised)

    # Confirm for multiple calls to the same method with different arguments,
    # that the attributes are updated.
    def test_tmdb_set_attrs_to_values_attribute_multiple_calls(self):
        search = tmdb.Search()
        response = search.movie(query=MOVIEQUERY1)
        title1 = search.results[0]['original_title']
        response = search.movie(query=MOVIEQUERY2)
        title2 = search.results[0]['original_title']
        self.assertNotEqual(title1, title2)
