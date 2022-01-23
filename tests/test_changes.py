# -*- coding: utf-8 -*-

"""
test_changes.py
~~~~~~~~~~~~~~~

This test suite checks the methods of the Changes class of tmdbsimple.

Created by Celia Oakley on 2013-11-05

:copyright: (c) 2013-2022 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

import unittest
import tmdbsimple as tmdb

from tests import API_KEY
tmdb.API_KEY = API_KEY


class ChangesTestCase(unittest.TestCase):
    def test_changes_movie(self):
        changes = tmdb.Changes()
        changes.movie()
        self.assertTrue(hasattr(changes, 'results'))

    def test_changes_tv(self):
        change = tmdb.Changes()
        change.tv()
        self.assertTrue(hasattr(change, 'results'))

    def test_changes_person(self):
        change = tmdb.Changes()
        change.person()
        self.assertTrue(hasattr(change, 'results'))
