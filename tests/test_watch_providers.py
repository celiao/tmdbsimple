# -*- coding: utf-8 -*-

"""
test_watch_providers.py
~~~~~~~~~~~~~~~~~~~~~

This test suite checks the methods of the WatchProviders class of tmdbsimple.

Created by lardbit on 2024-09-02

:copyright: (c) 2013-2022 by Celia Oakley.
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

    def test_regions(self):
        watch_providers = tmdb.WatchProviders()
        response = watch_providers.watch_providers_available_regions()
        # Regions are two uppercase letters
        self.assertTrue(re.match('^[A-Z]{2}$', response.get('results', [])[0][ISO_3166_1]))

    def test_watch_providers_movie_list(self):
        watch_providers = tmdb.WatchProviders()
        response = watch_providers.watch_providers_movie_list()
        self.assertTrue(response.get('results', [])[0].get('provider_name'))

    def test_watch_providers_tv_list(self):
        watch_providers = tmdb.WatchProviders()
        response = watch_providers.watch_providers_tv_list()
        self.assertTrue(response.get('results', [])[0].get('provider_name'))
