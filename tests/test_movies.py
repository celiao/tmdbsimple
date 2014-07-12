# -*- coding: utf-8 -*- 
"""
test_movies.py
~~~~~~~~~~~~~~

This test suite checks the methods of the Movies class of tmdbsimple.

Created by Celia Oakley on 2013-11-05

:copyright: (c) 2013-2014 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

import unittest
import tmdbsimple as tmdb

from tests import API_KEY, SESSION_ID
tmdb.API_KEY = API_KEY

"""
Constants
"""
MOVIE_ID = 103332
MOVIE_TITLE = 'Ruby Sparks'
MOVIE_TITLE_FRENCH = "Elle s'appelle Ruby"
MOVIE_ID_ALTERNATIVE = 550
RATING = 7.5
COLLECTION_ID = 10
COLLECTION_NAME = 'Star Wars Collection'
COMPANY_ID = 1
COMPANY_NAME = 'Lucasfilm'
KEYWORD_ID = 1721
KEYWORD_NAME = 'fight'
REVIEW_ID = '5013bc76760ee372cb00253e'
REVIEW_AUTHOR = 'Chris'

"""
Status Codes
"""
SUCCESSFUL_UPDATE = 12


class MoviesTestCase(unittest.TestCase):
    def test_movies_info(self):
        id = MOVIE_ID
        title = MOVIE_TITLE
        movie = tmdb.Movies(id)
        response = movie.info()
        self.assertEqual(movie.title, title)

    def test_movies_info_with_params(self):
        id = MOVIE_ID
        title = MOVIE_TITLE_FRENCH
        movie = tmdb.Movies(id)
        response = movie.info(language='fr')
        self.assertEqual(movie.title, title)

    def test_movies_alternative_titles(self):
        id = MOVIE_ID_ALTERNATIVE
        movie = tmdb.Movies(id)
        response = movie.alternative_titles()
        self.assertTrue(hasattr(movie, 'titles'))

    def test_movies_credits(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        response = movie.credits()
        self.assertTrue(hasattr(movie, 'cast'))

    def test_movies_images(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        response = movie.images()
        self.assertTrue(hasattr(movie, 'backdrops'))

    def test_movies_keywords(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        response = movie.keywords()
        self.assertTrue(hasattr(movie, 'keywords'))

    def test_movies_releases(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        response = movie.releases()
        self.assertTrue(hasattr(movie, 'countries'))

    def test_movies_videos(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        response = movie.videos()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_translations(self):
        id = MOVIE_ID_ALTERNATIVE
        movie = tmdb.Movies(id)
        response = movie.translations()
        self.assertTrue(hasattr(movie, 'translations'))

    def test_movies_similar_movies(self):
        id = MOVIE_ID_ALTERNATIVE
        movie = tmdb.Movies(id)
        response = movie.similar_movies()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_reviews(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        response = movie.reviews()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_lists(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        response = movie.lists()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_changes(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        response = movie.changes()
        self.assertTrue(hasattr(movie, 'changes'))

    def test_movies_latest(self):
        movie = tmdb.Movies()
        response = movie.latest()
        self.assertTrue(hasattr(movie, 'popularity'))

    def test_movies_upcoming(self):
        movie = tmdb.Movies()
        response = movie.upcoming()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_now_playing(self):
        movie = tmdb.Movies()
        response = movie.now_playing()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_popular(self):
        movie = tmdb.Movies()
        response = movie.popular()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_top_rated(self):
        movie = tmdb.Movies()
        response = movie.top_rated()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_account_states(self):
        id = MOVIE_ID_ALTERNATIVE
        movie = tmdb.Movies(id)
        response = movie.account_states(session_id=SESSION_ID)
        self.assertTrue(hasattr(movie, 'favorite'))

    def test_movies_rating(self):
        id = MOVIE_ID
        status_code = SUCCESSFUL_UPDATE
        movie = tmdb.Movies(id)
        response = movie.rating(session_id=SESSION_ID, value=RATING)
        self.assertEqual(movie.status_code, status_code)


class CollectionsTestCase(unittest.TestCase):
    def test_collections_info(self):
        id = COLLECTION_ID
        name = COLLECTION_NAME
        collection = tmdb.Collections(id)
        response = collection.info()
        self.assertEqual(collection.name, name)

    def test_collections_images(self):
        id = COLLECTION_ID
        collection = tmdb.Collections(id)
        response = collection.images()
        self.assertTrue(hasattr(collection, 'parts'))


class CompaniesTestCase(unittest.TestCase):
    def test_companies_info(self):
        id = COMPANY_ID
        name = COMPANY_NAME
        company = tmdb.Companies(id)
        response = company.info()
        self.assertEqual(company.name, name)

    def test_companies_movies(self):
        id = COMPANY_ID
        company = tmdb.Companies(id)
        response = company.movies()
        self.assertTrue(hasattr(company, 'results'))


class KeywordsTestCase(unittest.TestCase):
    def test_keywords_info(self):
        id = KEYWORD_ID
        name = KEYWORD_NAME
        keyword = tmdb.Keywords(id)
        response = keyword.info()
        self.assertEqual(keyword.name, name)

    def test_keywords_movies(self):
        id = KEYWORD_ID
        keyword = tmdb.Keywords(id)
        response = keyword.movies()
        self.assertTrue(hasattr(keyword, 'results'))


class ReviewsTestCase(unittest.TestCase):
    def test_reviews_info(self):
        id = REVIEW_ID
        author = REVIEW_AUTHOR
        review = tmdb.Reviews(id)
        response = review.info()
        self.assertEqual(review.author, author)

