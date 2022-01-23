# -*- coding: utf-8 -*-

"""
test_people.py
~~~~~~~~~~~~~~

This test suite checks the methods of the People class of tmdbsimple.

Created by Celia Oakley on 2013-11-05

:copyright: (c) 2013-2022 by Celia Oakley.
:license: GPLv3, see LICENSE for more details.
"""

import unittest
import tmdbsimple as tmdb

from tests import API_KEY
tmdb.API_KEY = API_KEY

"""
Constants
"""
PEOPLE_ID = 287
PEOPLE_NAME = 'Brad Pitt'
CREDITS_ID = '52542282760ee313280017f9'
CREDITS_DEPARTMENT = 'Acting'


class PeopleTestCase(unittest.TestCase):
    def test_people_info(self):
        id = PEOPLE_ID
        name = PEOPLE_NAME
        person = tmdb.People(id)
        person.info()
        self.assertEqual(person.name, name)

    def test_people_changes(self):
        id = PEOPLE_ID
        person = tmdb.People(id)
        person.changes()
        self.assertTrue(hasattr(person, 'changes'))

    def test_people_movie_credits(self):
        id = PEOPLE_ID
        person = tmdb.People(id)
        person.movie_credits()
        self.assertTrue(hasattr(person, 'cast'))

    def test_people_tv_credits(self):
        id = PEOPLE_ID
        person = tmdb.People(id)
        person.tv_credits()
        self.assertTrue(hasattr(person, 'cast'))

    def test_people_combined_credits(self):
        id = PEOPLE_ID
        person = tmdb.People(id)
        person.combined_credits()
        self.assertTrue(hasattr(person, 'cast'))

    def test_people_external_ids(self):
        id = PEOPLE_ID
        person = tmdb.People(id)
        person.external_ids()
        self.assertTrue(hasattr(person, 'tvrage_id'))

    def test_people_images(self):
        id = PEOPLE_ID
        person = tmdb.People(id)
        person.images()
        self.assertTrue(hasattr(person, 'profiles'))

    def test_people_tagged_images(self):
        id = PEOPLE_ID
        person = tmdb.People(id)
        person.tagged_images()
        self.assertTrue(hasattr(person, 'results'))

    def test_people_translations(self):
        id = PEOPLE_ID
        person = tmdb.People(id)
        person.translations()
        self.assertTrue(hasattr(person, 'translations'))

    def test_people_latest(self):
        person = tmdb.People()
        person.latest()
        self.assertTrue(hasattr(person, 'name'))

    def test_people_popular(self):
        person = tmdb.People()
        person.popular()
        self.assertTrue(hasattr(person, 'results'))


class CreditsTestCase(unittest.TestCase):
    def test_credits_info(self):
        id = CREDITS_ID
        department = CREDITS_DEPARTMENT
        credit = tmdb.Credits(id)
        credit.info()
        self.assertEqual(credit.department, department)
