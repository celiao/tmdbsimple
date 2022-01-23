# -*- coding: utf-8 -*-

"""
test_account.py
~~~~~~~~~~~~~~~

This test suite checks the methods of the Account class of tmdbsimple.

Created by Celia Oakley on 2013-11-05

:copyright: (c) 2013-2022 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

import unittest
import tmdbsimple as tmdb

from tests import API_KEY, SESSION_ID, USERNAME, PASSWORD
tmdb.API_KEY = API_KEY

"""
Constants
"""
MOVIETITLE = 'The Brother from Another Planet'
TVTITLE = 'Breaking Bad'
FAVORITE_MOVIE_ID = 62211
WATCHLIST_MEDIA_ID = 11
LIST_ID = '509ec17b19c2950a0600050d'
LIST_CREATED_BY = 'travisbell'
LIST_MOVIE_ID = 76203    # Argo
LIST_NAME = 'My newly created list'
LIST_DESCRIPTION = 'No duplicates here'
LIST_LANGUAGE = 'de'
LIST_ITEM_MEDIA_ID = 550

"""
Status codes and messages
"""
SUCCESS_PERIOD = 'The item/record was created successfully.'
SUCCESSFUL_UPDATE = 12
SUCCESSFUL_REMOVE_ITEM = 13
SUCCESSFUL_DELETE = 12


class AccountTestCase(unittest.TestCase):
    # run this test with a valid session_id and authenticated account
    def test_account_info(self):
        username = USERNAME
        account = tmdb.Account(SESSION_ID)
        account.info()
        self.assertEqual(account.username, username)

    def test_account_lists(self):
        account = tmdb.Account(SESSION_ID)
        account.info()    # to set account.id
        account.lists()
        self.assertTrue(hasattr(account, 'results'))

    def test_account_favorite_movies(self):
        movietitle = MOVIETITLE
        account = tmdb.Account(SESSION_ID)
        account.info()    # to set account.id
        account.favorite_movies()
        self.assertEqual(account.results[0]['title'], movietitle)

    def test_account_favorite_tv(self):
        tvtitle = TVTITLE
        account = tmdb.Account(SESSION_ID)
        account.info()    # to set account.id
        account.favorite_tv()
        self.assertEqual(account.results[0]['name'], tvtitle)

    def test_account_favorite(self):
        status_code = SUCCESSFUL_UPDATE
        account = tmdb.Account(SESSION_ID)
        account.info()    # to set account.id
        kwargs = {
            'media_type': 'movie',
            'movie_id': FAVORITE_MOVIE_ID,
            'favorite': True,
        }
        account.favorite(**kwargs)
        self.assertEqual(account.status_code, status_code)

    def test_account_rated_movies(self):
        account = tmdb.Account(SESSION_ID)
        account.info()    # to set account.id
        kwargs = {'page': 1, 'sort_by': 'created_at.asc'}
        account.rated_movies(**kwargs)
        self.assertTrue(hasattr(account, 'results'))

    def test_account_rated_tv(self):
        account = tmdb.Account(SESSION_ID)
        account.info()    # to set account.id
        kwargs = {'page': 1, 'sort_by': 'created_at.asc'}
        account.rated_tv(**kwargs)
        self.assertTrue(hasattr(account, 'results'))

    def test_account_rated_tv_episodes(self):
        account = tmdb.Account(SESSION_ID)
        account.info()    # to set account.id
        kwargs = {'page': 1, 'sort_by': 'created_at.asc'}
        account.rated_tv_episodes(**kwargs)
        self.assertTrue(hasattr(account, 'results'))

    def test_account_watchlist_movies(self):
        movietitle = MOVIETITLE
        account = tmdb.Account(SESSION_ID)
        account.info()    # to set account.id
        kwargs = {'page': 1, 'sort_by': 'created_at.asc'}
        account.watchlist_movies(**kwargs)
        self.assertEqual(account.results[0]['title'], movietitle)

    def test_account_watchlist_tv(self):
        tvtitle = TVTITLE
        account = tmdb.Account(SESSION_ID)
        account.info()    # to set account.id
        kwargs = {'page': 1, 'sort_by': 'created_at.asc'}
        account.watchlist_tv(**kwargs)
        self.assertEqual(account.results[0]['name'], tvtitle)

    def test_account_watchlist(self):
        status_code = SUCCESSFUL_UPDATE
        account = tmdb.Account(SESSION_ID)
        account.info()    # to set account.id
        kwargs = {
            'media_type': 'movie',
            'media_id': WATCHLIST_MEDIA_ID,
            'watchlist': 'true',
        }
        account.watchlist(**kwargs)
        self.assertEqual(account.status_code, status_code)


class AuthenticationTestCase(unittest.TestCase):
    def test_authentication_guest_session_new(self):
        success = True
        auth = tmdb.Authentication()
        auth.guest_session_new()
        self.assertEqual(auth.success, success)

    def test_authentication_token_new(self):
        success = True
        auth = tmdb.Authentication()
        auth.token_new()
        self.assertEqual(auth.success, success)

        # Example usage only.
        # User needs to approve request token, so would error here.
        # See https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id.
        # test_authentication_session_new(self):
        # kwargs = {'request_token': auth.request_token}
        # success = True
        # auth = tmdb.Authentication()
        # response = auth.session_new(**kwargs)
        # self.assertEqual(auth.success, success)

        # test_authentication_token_validate_with_login(self):
        kwargs = {
            'request_token': auth.request_token,
            'username': USERNAME,
            'password': PASSWORD,
        }
        success = True
        auth = tmdb.Authentication()
        auth.token_validate_with_login(**kwargs)
        self.assertEqual(auth.success, success)

        # Example usage only.
        # Don't want to delete session every time test is run.
        # test_session_delete(self):
        # kwargs = {'session_id': SESSION_ID}
        # success = True
        # auth = tmdb.Authentication()
        # response = auth.session_delete(**kwargs)
        # self.assertEqual(auth.success, success)


class GuestSessionsTestCase(unittest.TestCase):
    def test_guest_sessions_rated_movies(self):
        # get a guest session id
        auth = tmdb.Authentication()
        auth.guest_session_new()
        guest_session_id = auth.guest_session_id

        # get a list of rated movies for the guest session id
        guest_session = tmdb.GuestSessions(guest_session_id)
        guest_session.rated_movies()
        self.assertTrue(hasattr(guest_session, 'results'))

    def test_guest_sessions_rated_tv(self):
        # get a guest session id
        auth = tmdb.Authentication()
        auth.guest_session_new()
        guest_session_id = auth.guest_session_id

        # get a list of rated tv shows for the guest session id
        guest_session = tmdb.GuestSessions(guest_session_id)
        guest_session.rated_tv()
        self.assertTrue(hasattr(guest_session, 'results'))

    def test_guest_sessions_rated_tv_episodes(self):
        # get a guest session id
        auth = tmdb.Authentication()
        auth.guest_session_new()
        guest_session_id = auth.guest_session_id

        # get a list of rated tv episodes for the guest session id
        guest_session = tmdb.GuestSessions(guest_session_id)
        guest_session.rated_tv_episodes()
        self.assertTrue(hasattr(guest_session, 'results'))


class ListsTestCase(unittest.TestCase):
    def test_lists_info(self):
        id = LIST_ID
        created_by = LIST_CREATED_BY
        lst = tmdb.Lists(id)
        lst.info()
        self.assertEqual(lst.created_by, created_by)

    def test_lists_item_status(self):
        id = LIST_ID
        movie_id = LIST_MOVIE_ID
        lst = tmdb.Lists(id)
        lst.item_status(movie_id=movie_id)
        self.assertTrue(hasattr(lst, 'item_present'))

    def test_lists_create_add_remove_clear_delete(self):
        kwargs = {
            'name': LIST_NAME,
            'description': LIST_DESCRIPTION,
            'language': LIST_LANGUAGE,
        }
        status_message = SUCCESS_PERIOD
        lst = tmdb.Lists(0, SESSION_ID)
        lst.list_create(**kwargs)
        self.assertEqual(lst.status_message, status_message)

        status_code = SUCCESSFUL_UPDATE
        lst.add_item(media_id=LIST_ITEM_MEDIA_ID)
        self.assertEqual(lst.status_code, status_code)

        status_code = SUCCESSFUL_REMOVE_ITEM
        lst.remove_item(media_id=LIST_ITEM_MEDIA_ID)
        self.assertEqual(lst.status_code, status_code)

        status_code = SUCCESSFUL_UPDATE
        lst.list_clear(confirm='true')
        self.assertEqual(lst.status_code, status_code)

        # TODO: add list_delete check when list delete bug is fixed:
        # https://www.themoviedb.org/talk/5e7bb85aeec4f30018aa327c#5f0b5ff91f98d100361f3037.
        # Deletes list, but returns 500 error rather than 201.
        # status_code = SUCCESSFUL_DELETE
        # lst.list_delete()
        # self.assertEqual(lst.status_code, status_code)
