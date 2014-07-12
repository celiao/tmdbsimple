# -*- coding: utf-8 -*-

"""
test_configuration.py
~~~~~~~~~~~~~~~~~~~~~

This test suite checks the methods of the Configuration class of tmdbsimple.

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
CHANGE_KEYS = ['adult', 'also_known_as', 'alternative_titles', \
    'biography', 'birthday', 'budget', 'cast', 'character_names', \
    'crew', 'deathday', 'general', 'genres', 'homepage', 'images', \
    'imdb_id', 'name', 'original_title', 'overview', 'plot_keywords', \
    'production_companies', 'production_countries', 'releases', \
    'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', \
    'title', 'trailers', 'translations']

class ConfigurationTestCase(unittest.TestCase):
    def test_configuration_info(self):
        change_keys = CHANGE_KEYS
        config = tmdb.Configuration()
        response = config.info()
        self.assertEqual(config.change_keys, change_keys)

        # Also test that bad API_KEY results in exception
        # Restore key for sequential tests
        api_key_save = tmdb.API_KEY
        tmdb.API_KEY = 0
        config = tmdb.Configuration()
        self.assertRaises(tmdb.APIKeyError, config.info)
        tmdb.API_KEY = api_key_save


class CertificationsTestCase(unittest.TestCase):
    def test_certifications_list(self):
        certifications = tmdb.Certifications()
        response = certifications.list()
        self.assertTrue(hasattr(certifications, 'certifications'))


class TimezonesTestCase(unittest.TestCase):
    def test_timezones_list(self):
        timezones = tmdb.Timezones()
        response = timezones.list()
        timezone_keys = list(response[0].keys())
        self.assertEqual(timezone_keys[0], 'AD')


