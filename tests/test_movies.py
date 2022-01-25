# -*- coding: utf-8 -*-
"""
test_movies.py
~~~~~~~~~~~~~~

This test suite checks the methods of the Movies class of tmdbsimple.

Created by Celia Oakley on 2013-11-05

:copyright: (c) 2013-2022 by Celia Oakley.
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
MOVIE_TITLE_GERMAN = 'Ruby Sparks - Meine fabelhafte Freundin'
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
SUCCESSFUL_CREATE = 1
SUCCESSFUL_UPDATE = 12
SUCCESSFUL_DELETE = 13


class MoviesTestCase(unittest.TestCase):
    def test_movies_info(self):
        id = MOVIE_ID
        title = MOVIE_TITLE
        movie = tmdb.Movies(id)
        movie.info()
        self.assertEqual(movie.title, title)

    def test_movies_info_with_params(self):
        id = MOVIE_ID
        title = MOVIE_TITLE_GERMAN
        movie = tmdb.Movies(id)
        movie.info(language='de')
        self.assertEqual(movie.title, title)

    def test_movies_account_states(self):
        id = MOVIE_ID_ALTERNATIVE
        movie = tmdb.Movies(id)
        movie.account_states(session_id=SESSION_ID)
        self.assertTrue(hasattr(movie, 'favorite'))

    def test_movies_alternative_titles(self):
        id = MOVIE_ID_ALTERNATIVE
        movie = tmdb.Movies(id)
        movie.alternative_titles()
        self.assertTrue(hasattr(movie, 'titles'))

    def test_movies_changes(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        movie.changes()
        self.assertTrue(hasattr(movie, 'changes'))

    def test_movies_credits(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        movie.credits()
        self.assertTrue(hasattr(movie, 'cast'))

    def test_movies_external_ids(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        movie.external_ids()
        self.assertTrue(hasattr(movie, 'imdb_id'))

    def test_movies_images(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        movie.images()
        self.assertTrue(hasattr(movie, 'backdrops'))

    def test_movies_keywords(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        movie.keywords()
        self.assertTrue(hasattr(movie, 'keywords'))

    def test_movies_lists(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        movie.lists()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_recommendations(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        movie.recommendations()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_release_dates(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        movie.release_dates()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_reviews(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        movie.reviews()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_similar_movies(self):
        id = MOVIE_ID_ALTERNATIVE
        movie = tmdb.Movies(id)
        movie.similar_movies()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_translations(self):
        id = MOVIE_ID_ALTERNATIVE
        movie = tmdb.Movies(id)
        movie.translations()
        self.assertTrue(hasattr(movie, 'translations'))

    def test_movies_videos(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        movie.videos()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_watch_providers(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        movie.watch_providers()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_rating_and_rating_delete(self):
        status_code_create = SUCCESSFUL_CREATE
        status_code_update = SUCCESSFUL_UPDATE
        status_code_delete = SUCCESSFUL_DELETE
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        movie.rating(session_id=SESSION_ID, value=RATING)
        self.assertTrue(movie.status_code == status_code_create
                        or movie.status_code == status_code_update)
        movie.rating_delete(session_id=SESSION_ID)
        self.assertEqual(movie.status_code, status_code_delete)

    def test_movies_latest(self):
        movie = tmdb.Movies()
        movie.latest()
        self.assertTrue(hasattr(movie, 'popularity'))

    def test_movies_now_playing(self):
        movie = tmdb.Movies()
        movie.now_playing()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_popular(self):
        movie = tmdb.Movies()
        movie.popular()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_top_rated(self):
        movie = tmdb.Movies()
        movie.top_rated()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_upcoming(self):
        movie = tmdb.Movies()
        movie.upcoming()
        self.assertTrue(hasattr(movie, 'results'))

    def test_movies_releases(self):
        id = MOVIE_ID
        movie = tmdb.Movies(id)
        movie.releases()
        self.assertTrue(hasattr(movie, 'countries'))


class CollectionsTestCase(unittest.TestCase):
    def test_collections_info(self):
        id = COLLECTION_ID
        name = COLLECTION_NAME
        collection = tmdb.Collections(id)
        collection.info()
        self.assertEqual(collection.name, name)

    def test_collections_images(self):
        id = COLLECTION_ID
        collection = tmdb.Collections(id)
        collection.images()
        self.assertTrue(hasattr(collection, 'backdrops'))

    def test_collections_translations(self):
        id = COLLECTION_ID
        collection = tmdb.Collections(id)
        collection.translations()
        self.assertTrue(hasattr(collection, 'translations'))


class CompaniesTestCase(unittest.TestCase):
    def test_companies_info(self):
        id = COMPANY_ID
        name = COMPANY_NAME
        company = tmdb.Companies(id)
        company.info()
        self.assertEqual(company.name, name)

    def test_companies_alternative_names(self):
        id = COMPANY_ID
        company = tmdb.Companies(id)
        company.alternative_names()
        self.assertTrue(hasattr(company, 'results'))

    def test_companies_images(self):
        id = COMPANY_ID
        company = tmdb.Companies(id)
        company.images()
        self.assertTrue(hasattr(company, 'logos'))

    def test_companies_movies(self):
        id = COMPANY_ID
        company = tmdb.Companies(id)
        company.movies()
        self.assertTrue(hasattr(company, 'results'))


class KeywordsTestCase(unittest.TestCase):
    def test_keywords_info(self):
        id = KEYWORD_ID
        name = KEYWORD_NAME
        keyword = tmdb.Keywords(id)
        keyword.info()
        self.assertEqual(keyword.name, name)

    def test_keywords_movies(self):
        id = KEYWORD_ID
        keyword = tmdb.Keywords(id)
        keyword.movies()
        self.assertTrue(hasattr(keyword, 'results'))


class ReviewsTestCase(unittest.TestCase):
    def test_reviews_info(self):
        id = REVIEW_ID
        author = REVIEW_AUTHOR
        review = tmdb.Reviews(id)
        review.info()
        self.assertEqual(review.author, author)
