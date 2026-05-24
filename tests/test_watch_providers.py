# -*- coding: utf-8 -*-

"""
test_watch_providers.py
~~~~~~~~~~~~~~~~~~~~~~~

This test suite checks the methods of the WatchProviders class of tmdbsimple.

Created by Celia Oakley on 2026-05-24

:copyright: (c) 2013-2026 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

import unittest
import re
import tmdbsimple as tmdb

from tests import API_KEY
tmdb.API_KEY = API_KEY

"""
Constants
"""
ISO_3166_1 = 'iso_3166_1'


class WatchProvidersTestCase(unittest.TestCase):
    def test_watch_providers_regions(self):
        watch_providers = tmdb.WatchProviders()
        response = watch_providers.regions()
        # Regions are two uppercase letters
        self.assertTrue(re.match('^[A-Z]{2}$',
                                 response['results'][0][ISO_3166_1]))

    def test_watch_providers_movie(self):
        watch_providers = tmdb.WatchProviders()
        response = watch_providers.movie()
        self.assertTrue(response['results'][0]['provider_name'])

    def test_watch_providers_tv(self):
        watch_providers = tmdb.WatchProviders()
        response = watch_providers.tv()
        self.assertTrue(response['results'][0]['provider_name'])
