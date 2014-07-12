# -*- coding: utf-8 -*-

"""
test_tv.py
~~~~~~~~~~

This test suite checks the methods of the Test class of tmdbsimple.

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
TV_ID = 1396
TV_NAME = 'Breaking Bad'
TV_IMDB_ID = 'tt0903747'
RATING = 7.5
TV_SEASON_ID = 3572
TV_SEASON_NUMBER = 1
TV_SEASON_NAME = 'Season 1'
TV_SEASON_TVDB_ID = 2547
TV_EPISODE_NUMBER = 1
TV_EPISODE_NAME = 'Pilot'
TV_EPISODE_IMDB_ID = 'tt0959621'
NETWORK_ID = 49
NETWORK_NAME = 'HBO'


"""
Status codes and messages
"""
SUCCESSFUL_UPDATE = 12


class TVTestCase(unittest.TestCase):
    def test_tv_info(self):
        id = TV_ID
        name = TV_NAME
        tv = tmdb.TV(id)
        response = tv.info()
        self.assertEqual(tv.name, name)

    def test_tv_credits(self):
        id = TV_ID
        tv = tmdb.TV(id)
        response = tv.credits()
        self.assertTrue(hasattr(tv, 'cast'))

    def test_tv_external_ids(self):
        id = TV_ID
        imdb_id = TV_IMDB_ID
        tv = tmdb.TV(id)
        response = tv.external_ids()
        self.assertEqual(tv.imdb_id, imdb_id)

    def test_tv_images(self):
        id = TV_ID
        tv = tmdb.TV(id)
        response = tv.images()
        self.assertTrue(hasattr(tv, 'backdrops'))

    def test_tv_rating(self):
        id = TV_ID
        status_code = SUCCESSFUL_UPDATE
        tv = tmdb.TV(id)
        response = tv.rating(session_id=SESSION_ID, value=RATING)
        self.assertEqual(tv.status_code, status_code)

    def test_tv_translations(self):
        id = TV_ID
        tv = tmdb.TV(id)
        response = tv.translations()
        self.assertTrue(hasattr(tv, 'translations'))

    def test_tv_videos(self):
        id = TV_ID
        tv = tmdb.TV(id)
        response = tv.videos()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_on_the_air(self):
        tv = tmdb.TV()
        response = tv.on_the_air()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_airing_today(self):
        tv = tmdb.TV()
        response = tv.airing_today()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_top_rated(self):
        tv = tmdb.TV()
        response = tv.top_rated()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_popular(self):
        tv = tmdb.TV()
        response = tv.popular()
        self.assertTrue(hasattr(tv, 'results'))


class TVSeasonsTestCase(unittest.TestCase):
    def test_tv_seasons_info(self):
        id = TV_SEASON_ID
        season_number = TV_SEASON_NUMBER
        name = TV_SEASON_NAME
        tv_seasons = tmdb.TV_Seasons(id, season_number)
        response = tv_seasons.info()
        self.assertEqual(tv_seasons.name, name)

    def test_tv_seasons_credits(self):
        id = TV_SEASON_ID
        season_number = TV_SEASON_NUMBER
        tv_seasons = tmdb.TV_Seasons(id, season_number)
        response = tv_seasons.credits()
        self.assertTrue(hasattr(tv_seasons, 'crew'))

    def test_tv_seasons_external_ids(self):
        id = TV_SEASON_ID
        season_number = TV_SEASON_NUMBER
        tvdb_id = TV_SEASON_TVDB_ID
        tv_seasons = tmdb.TV_Seasons(id, season_number)
        response = tv_seasons.external_ids()
        self.assertEqual(tv_seasons.tvdb_id, tvdb_id)

    def test_tv_seasons_images(self):
        id = TV_SEASON_ID
        season_number = TV_SEASON_NUMBER
        tv_seasons = tmdb.TV_Seasons(id, season_number)
        response = tv_seasons.images()
        self.assertTrue(hasattr(tv_seasons, 'posters'))

    def test_tv_seasons_videos(self):
        id = TV_SEASON_ID
        season_number = TV_SEASON_NUMBER
        tv_seasons = tmdb.TV_Seasons(id, season_number)
        response = tv_seasons.videos()
        self.assertTrue(hasattr(tv_seasons, 'results'))


class TVEpisodesTestCase(unittest.TestCase):
    def test_tv_episodes_info(self):
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        name = TV_EPISODE_NAME
        tv_episodes = tmdb.TV_Episodes(series_id, season_number, episode_number)
        response = tv_episodes.info()
        response = tv_episodes.info()
        self.assertEqual(tv_episodes.name, name)

    def test_tv_episodes_credits(self):
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        tv_episodes = tmdb.TV_Episodes(series_id, season_number, episode_number)
        response = tv_episodes.credits()
        self.assertTrue(hasattr(tv_episodes, 'guest_stars'))

    def test_tv_episodes_external_ids(self):
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        imdb_id = TV_EPISODE_IMDB_ID
        tv_episodes = tmdb.TV_Episodes(series_id, season_number, episode_number)
        response = tv_episodes.external_ids()
        self.assertEqual(tv_episodes.imdb_id, imdb_id)

    def test_tv_episodes_images(self):
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        tv_episodes = tmdb.TV_Episodes(series_id, season_number, episode_number)
        response = tv_episodes.images()
        self.assertTrue(hasattr(tv_episodes, 'stills'))

    def test_tv_episodes_rating(self):
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        status_code = SUCCESSFUL_UPDATE
        tv_episodes = tmdb.TV_Episodes(series_id, season_number, episode_number)
        response = tv_episodes.rating(session_id=SESSION_ID, value=RATING)
        self.assertEqual(tv_episodes.status_code, status_code)

    def test_tv_episodes_videos(self):
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        status_code = SUCCESSFUL_UPDATE
        tv_episodes = tmdb.TV_Episodes(series_id, season_number, episode_number)
        response = tv_episodes.videos()
        self.assertTrue(hasattr(tv_episodes, 'results'))


class NetworksTestCase(unittest.TestCase):
    def test_networks_info(self):
        id = NETWORK_ID
        name = NETWORK_NAME
        network = tmdb.Networks(id)
        response = network.info()
        self.assertEqual(network.name, name)

