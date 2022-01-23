# -*- coding: utf-8 -*-

"""
test_genres.py
~~~~~~~~~~~~~~

This test suite checks the methods of the Genres class of tmdbsimple.

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
GENRE_ID = 18


class GenresTestCase(unittest.TestCase):
    def test_genres_movie_list(self):
        genre = tmdb.Genres()
        genre.movie_list()
        self.assertTrue(hasattr(genre, 'genres'))

    def test_genres_tv_list(self):
        genre = tmdb.Genres()
        genre.tv_list()
        self.assertTrue(hasattr(genre, 'genres'))

    def test_genres_movies(self):
        id = GENRE_ID
        genre = tmdb.Genres(id)
        genre.movies()
        self.assertTrue(hasattr(genre, 'results'))
