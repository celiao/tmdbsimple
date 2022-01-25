# -*- coding: utf-8 -*-

"""
test_tv.py
~~~~~~~~~~

This test suite checks the methods of the Test class of tmdbsimple.

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
TV_ID = 1396
TV_NAME = 'Breaking Bad'
TV_IMDB_ID = 'tt0903747'
RATING = 7.5
TV_SEASON_ID = 3572
TV_SEASON_NUMBER = 1
TV_SEASON_NAME = 'Season 1'
TV_SEASON_TVDB_ID = 2547
TV_EPISODE_ID = 62085
TV_EPISODE_NUMBER = 1
TV_EPISODE_NAME = 'Pilot'
TV_EPISODE_IMDB_ID = 'tt0959621'
TV_EPISODE_GROUP_ID = '5acf93e60e0a26346d0000ce'
NETWORK_ID = 49
NETWORK_NAME = 'HBO'


"""
Status codes and messages
"""
SUCCESSFUL_CREATE = 1
SUCCESSFUL_UPDATE = 12
SUCCESSFUL_DELETE = 13


class TVTestCase(unittest.TestCase):
    def test_tv_info(self):
        id = TV_ID
        name = TV_NAME
        tv = tmdb.TV(id)
        tv.info()
        self.assertEqual(tv.name, name)

    def test_tv_account_states(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.account_states(session_id=SESSION_ID)
        self.assertTrue(hasattr(tv, 'rated'))

    def test_tv_alternative_titles(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.alternative_titles()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_content_ratings(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.content_ratings()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_credits(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.credits()
        self.assertTrue(hasattr(tv, 'cast'))

    def test_tv_episode_groups(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.episode_groups()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_external_ids(self):
        id = TV_ID
        imdb_id = TV_IMDB_ID
        tv = tmdb.TV(id)
        tv.external_ids()
        self.assertEqual(tv.imdb_id, imdb_id)

    def test_tv_images(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.images()
        self.assertTrue(hasattr(tv, 'backdrops'))

    def test_tv_keywords(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.keywords()
        self.assertTrue(hasattr(tv, 'keywords'))

    def test_tv_recommendations(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.recommendations()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_reviews(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.reviews()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_screened_theatrically(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.screened_theatrically()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_similar(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.similar()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_translations(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.translations()
        self.assertTrue(hasattr(tv, 'translations'))

    def test_tv_videos(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.videos()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_watch_providers(self):
        id = TV_ID
        tv = tmdb.TV(id)
        tv.watch_providers()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_rating_and_rating_delete(self):
        status_code_create = SUCCESSFUL_CREATE
        status_code_update = SUCCESSFUL_UPDATE
        status_code_delete = SUCCESSFUL_DELETE
        id = TV_ID
        tv = tmdb.TV(id)
        tv.rating(session_id=SESSION_ID, value=RATING)
        self.assertTrue(tv.status_code, status_code_create
                        or tv.status_code == status_code_update)
        tv.rating_delete(session_id=SESSION_ID)
        self.assertEqual(tv.status_code, status_code_delete)

    def test_tv_latest(self):
        tv = tmdb.TV()
        tv.latest()
        self.assertTrue(hasattr(tv, 'first_air_date'))

    def test_tv_airing_today(self):
        tv = tmdb.TV()
        tv.airing_today()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_on_the_air(self):
        tv = tmdb.TV()
        tv.on_the_air()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_popular(self):
        tv = tmdb.TV()
        tv.popular()
        self.assertTrue(hasattr(tv, 'results'))

    def test_tv_top_rated(self):
        tv = tmdb.TV()
        tv.top_rated()
        self.assertTrue(hasattr(tv, 'results'))


class TVSeasonsTestCase(unittest.TestCase):
    def test_tv_seasons_info(self):
        series_id = TV_SEASON_ID
        season_number = TV_SEASON_NUMBER
        name = TV_SEASON_NAME
        tv_seasons = tmdb.TV_Seasons(series_id, season_number)
        tv_seasons.info()
        self.assertEqual(tv_seasons.name, name)

    def test_tv_seasons_account_states(self):
        series_id = TV_SEASON_ID
        season_number = TV_SEASON_NUMBER
        tv_seasons = tmdb.TV_Seasons(series_id, season_number)
        tv_seasons.account_states(session_id=SESSION_ID)
        self.assertTrue(hasattr(tv_seasons, 'results'))

    def test_tv_seasons_credits(self):
        series_id = TV_SEASON_ID
        season_number = TV_SEASON_NUMBER
        tv_seasons = tmdb.TV_Seasons(series_id, season_number)
        tv_seasons.credits()
        self.assertTrue(hasattr(tv_seasons, 'crew'))

    def test_tv_seasons_external_ids(self):
        series_id = TV_SEASON_ID
        season_number = TV_SEASON_NUMBER
        tvdb_id = TV_SEASON_TVDB_ID
        tv_seasons = tmdb.TV_Seasons(series_id, season_number)
        tv_seasons.external_ids()
        self.assertEqual(tv_seasons.tvdb_id, tvdb_id)

    def test_tv_seasons_images(self):
        series_id = TV_SEASON_ID
        season_number = TV_SEASON_NUMBER
        tv_seasons = tmdb.TV_Seasons(series_id, season_number)
        tv_seasons.images()
        self.assertTrue(hasattr(tv_seasons, 'posters'))

    def test_tv_seasons_videos(self):
        series_id = TV_SEASON_ID
        season_number = TV_SEASON_NUMBER
        tv_seasons = tmdb.TV_Seasons(series_id, season_number)
        tv_seasons.videos()
        self.assertTrue(hasattr(tv_seasons, 'results'))


class TVEpisodesTestCase(unittest.TestCase):
    def test_tv_episodes_info(self):
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        name = TV_EPISODE_NAME
        tv_episode = tmdb.TV_Episodes(series_id, season_number, episode_number)
        tv_episode.info()
        self.assertEqual(tv_episode.name, name)

    def test_tv_episodes_account_states(self):
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        tv_episode = tmdb.TV_Episodes(series_id, season_number, episode_number)
        tv_episode.account_states(session_id=SESSION_ID)
        self.assertTrue(hasattr(tv_episode, 'rated'))

    def test_tv_episodes_credits(self):
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        tv_episode = tmdb.TV_Episodes(series_id, season_number, episode_number)
        tv_episode.credits()
        self.assertTrue(hasattr(tv_episode, 'guest_stars'))

    def test_tv_episodes_external_ids(self):
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        imdb_id = TV_EPISODE_IMDB_ID
        tv_episode = tmdb.TV_Episodes(series_id, season_number, episode_number)
        tv_episode.external_ids()
        self.assertEqual(tv_episode.imdb_id, imdb_id)

    def test_tv_episodes_images(self):
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        tv_episode = tmdb.TV_Episodes(series_id, season_number, episode_number)
        tv_episode.images()
        self.assertTrue(hasattr(tv_episode, 'stills'))

    def test_tv_episodes_translations(self):
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        tv_episode = tmdb.TV_Episodes(series_id, season_number, episode_number)
        tv_episode.translations()
        self.assertTrue(hasattr(tv_episode, 'translations'))

    def test_tv_episodes_rating(self):
        status_code_create = SUCCESSFUL_CREATE
        status_code_update = SUCCESSFUL_UPDATE
        status_code_delete = SUCCESSFUL_DELETE
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        tv_episode = tmdb.TV_Episodes(series_id, season_number, episode_number)
        tv_episode.rating(session_id=SESSION_ID, value=RATING)
        self.assertTrue(tv_episode.status_code == status_code_create
                        or tv_episode.status_code == status_code_update)
        tv_episode.rating_delete(session_id=SESSION_ID)
        self.assertEqual(tv_episode.status_code, status_code_delete)

    def test_tv_episodes_videos(self):
        series_id = TV_ID
        season_number = TV_SEASON_NUMBER
        episode_number = TV_EPISODE_NUMBER
        tv_episode = tmdb.TV_Episodes(series_id, season_number, episode_number)
        tv_episode.videos()
        self.assertTrue(hasattr(tv_episode, 'results'))


class TVEpisodeGroupsTestCase(unittest.TestCase):
    def test_tv_episode_groups_info(self):
        tv_episode_group_id = TV_EPISODE_GROUP_ID
        tv_episode_group = tmdb.TV_Episode_Groups(tv_episode_group_id)
        tv_episode_group.info()
        self.assertTrue(hasattr(tv_episode_group, 'groups'))


class TVChangesTestCase(unittest.TestCase):
    def test_series_changes(self):
        id = TV_ID
        tv_changes = tmdb.TV_Changes(id)
        tv_changes.series()
        self.assertTrue(hasattr(tv_changes, 'changes'))

    def test_season_changes(self):
        id = TV_SEASON_ID
        tv_changes = tmdb.TV_Changes(id)
        tv_changes.season()
        self.assertTrue(hasattr(tv_changes, 'changes'))

    def test_episode_changes(self):
        id = TV_EPISODE_ID
        tv_changes = tmdb.TV_Changes(id)
        tv_changes.episode()
        self.assertTrue(hasattr(tv_changes, 'changes'))


class NetworksTestCase(unittest.TestCase):
    def test_networks_info(self):
        id = NETWORK_ID
        name = NETWORK_NAME
        network = tmdb.Networks(id)
        network.info()
        self.assertEqual(network.name, name)

    def test_networks_alternative_names(self):
        id = NETWORK_ID
        network = tmdb.Networks(id)
        network.alternative_names()
        self.assertTrue(hasattr(network, 'results'))

    def test_networks_images(self):
        id = NETWORK_ID
        network = tmdb.Networks(id)
        network.images()
        self.assertTrue(hasattr(network, 'logos'))
