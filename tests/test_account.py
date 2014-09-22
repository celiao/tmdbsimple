# -*- coding: utf-8 -*-

"""
test_account.py
~~~~~~~~~~~~~~~

This test suite checks the methods of the Account class of tmdbsimple.

Created by Celia Oakley on 2013-11-05

:copyright: (c) 2013-2014 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

import unittest
import tmdbsimple as tmdb

from tests import API_KEY, SESSION_ID, USERNAME, PASSWORD
tmdb.API_KEY = API_KEY

"""
Constants
"""
MOVIETITLE = 'The Brother From Another Planet'
TVTITLE = 'Breaking Bad'
FAVORITE_MOVIE_ID = 62211
WATCHLIST_MEDIA_ID = 11
LIST_ID = '509ec17b19c2950a0600050d'
LIST_CREATED_BY = 'Travis Bell'
LIST_MOVIE_ID = 76203 # Argo
LIST_NAME = 'My newly created list'
LIST_DESCRIPTION = 'No duplicates here'
LIST_ITEM_MEDIA_ID = 550

"""
Status codes and messages
"""
SUCCESSFUL_UPDATE = 12
SUCCESSFUL_DELETE = 13
SUCCESS_PERIOD = 'Success.'


class AccountTestCase(unittest.TestCase):
    # run this test with a valid session_id and authenticated account
    def test_account_info(self):
        username = USERNAME
        acct = tmdb.Account(SESSION_ID)
        response = acct.info()
        self.assertEqual(acct.username, username)

    def test_account_lists(self):
        acct = tmdb.Account(SESSION_ID)
        response = acct.info() # to set acct.id
        response = acct.lists()
        self.assertTrue(hasattr(acct, 'results'))

    def test_account_favorite_movies(self):
        movietitle = MOVIETITLE
        acct = tmdb.Account(SESSION_ID)
        response = acct.info() # to set acct.id
        response = acct.favorite_movies()
        self.assertEqual(acct.results[0]['title'], movietitle)

    def test_account_favorite_tv(self):
        tvtitle = TVTITLE
        acct = tmdb.Account(SESSION_ID)
        response = acct.info() # to set acct.id
        response = acct.favorite_tv()
        self.assertEqual(acct.results[0]['name'], tvtitle)

    def test_account_favorite(self):
        status_code = SUCCESSFUL_UPDATE
        acct = tmdb.Account(SESSION_ID)
        response = acct.info() # to set acct.id
        kwargs = {
            'media_type': 'movie', 
            'movie_id': FAVORITE_MOVIE_ID, 
            'favorite': True,
        }
        response = acct.favorite(**kwargs)
        self.assertEqual(acct.status_code, status_code)

    def test_account_rated_movies(self):
        acct = tmdb.Account(SESSION_ID)
        response = acct.info() # to set acct.id
        kwargs = {'page': 1, 'sort_by': 'created_at.asc'}
        response = acct.rated_movies(**kwargs)
        self.assertTrue(hasattr(acct, 'results'))

    def test_account_rated_tv(self):
        acct = tmdb.Account(SESSION_ID)
        response = acct.info() # to set acct.id
        kwargs = {'page': 1, 'sort_by': 'created_at.asc'}
        response = acct.rated_tv(**kwargs)
        self.assertTrue(hasattr(acct, 'results'))

    def test_account_watchlist_movies(self):
        movietitle = MOVIETITLE
        acct = tmdb.Account(SESSION_ID)
        response = acct.info() # to set acct.id
        kwargs = {'page': 1, 'sort_by': 'created_at.asc'}
        response = acct.watchlist_movies(**kwargs)
        self.assertEqual(acct.results[0]['title'], movietitle)

    def test_account_watchlist_tv(self):
        tvtitle = TVTITLE
        acct = tmdb.Account(SESSION_ID)
        response = acct.info() # to set acct.id
        kwargs = {'page': 1, 'sort_by': 'created_at.asc'}
        response = acct.watchlist_tv(**kwargs)
        self.assertEqual(acct.results[0]['name'], tvtitle)

    def test_account_watchlist(self):
        status_code = SUCCESSFUL_UPDATE
        acct = tmdb.Account(SESSION_ID)
        response = acct.info() # to set acct.id
        kwargs = {
            'media_type': 'movie', 
            'media_id': WATCHLIST_MEDIA_ID, 
            'watchlist': 'true',
        }
        response = acct.watchlist(**kwargs)
        self.assertEqual(acct.status_code, status_code)


class AuthenticationTestCase(unittest.TestCase):
    def test_authentication_token_new(self):
        success = True
        auth = tmdb.Authentication()
        response = auth.token_new()
        #print(auth.request_token)
        self.assertEqual(auth.success, success)

        # test_authentication_token_validate_with_login(self):
        kwargs = {
            'request_token': auth.request_token,
            'username': USERNAME,
            'password': PASSWORD,
        }
        success = True
        auth = tmdb.Authentication()
        response = auth.token_validate_with_login(**kwargs)
        self.assertEqual(auth.success, success)

        # test_authentication_session_new(self):
        kwargs = {'request_token': auth.request_token}
        success = True
        auth = tmdb.Authentication()
        response = auth.session_new(**kwargs)
        #print(auth.session_id)
        self.assertEqual(auth.success, success)

    def test_authentication_guest_session_new(self):
        success = True
        auth = tmdb.Authentication()
        response = auth.guest_session_new()
        self.assertEqual(auth.success, success)


class GuestSessionsTestCase(unittest.TestCase):
    def test_guest_sessions_rated_movies(self):
        # get a guest session id
        auth = tmdb.Authentication()
        response = auth.guest_session_new()
        guest_session_id = auth.guest_session_id

        # get a list of rated movies for the guest session id 
        guest_session = tmdb.GuestSessions(guest_session_id)
        response = guest_session.rated_movies()
        self.assertTrue(hasattr(guest_session, 'results'))


class ListsTestCase(unittest.TestCase):
    def test_lists_info(self):
        id = LIST_ID
        created_by = LIST_CREATED_BY
        lst = tmdb.Lists(id)
        response = lst.info()
        self.assertEqual(lst.created_by, created_by)

    def test_lists_item_status(self):
        id = LIST_ID
        movie_id = LIST_MOVIE_ID
        lst = tmdb.Lists(id)
        response = lst.item_status(movie_id=movie_id)
        self.assertTrue(hasattr(lst, 'item_present'))

    def test_lists_create_add_remove_clear_delete(self):
        kwargs = {
            'name': LIST_NAME,
            'description': LIST_DESCRIPTION,
        }
        status_message = SUCCESS_PERIOD
        lst = tmdb.Lists(0, SESSION_ID)
        #print(lst.session_id)
        response = lst.create_list(**kwargs)
        self.assertEqual(lst.status_message, status_message)

        list_id = lst.list_id

        status_code = SUCCESSFUL_UPDATE
        lst = tmdb.Lists(list_id, SESSION_ID)
        response = lst.add_item(media_id=LIST_ITEM_MEDIA_ID)
        self.assertEqual(lst.status_code, status_code)

        status_code = SUCCESSFUL_DELETE
        lst = tmdb.Lists(list_id, SESSION_ID)
        response = lst.remove_item(media_id=LIST_ITEM_MEDIA_ID)
        self.assertEqual(lst.status_code, status_code)

        status_code = SUCCESSFUL_UPDATE
        lst = tmdb.Lists(list_id, SESSION_ID)
        response = lst.clear_list(confirm='true')
        self.assertEqual(lst.status_code, status_code)

        status_code = SUCCESSFUL_DELETE
        lst = tmdb.Lists(list_id, SESSION_ID)
        response = lst.delete_list()
        self.assertEqual(lst.status_code, status_code)
