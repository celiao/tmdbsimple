# -*- coding: utf-8 -*-

"""
tmdbsimple.changes
~~~~~~~~~~~~~~~~~~
This module implements the Changes functionality of tmdbsimple.

Created by Celia Oakley on 2013-10-31.

:copyright: (c) 2013-2025 by Celia Oakley
:license: GPLv3, see LICENSE for more details
"""

from .base import TMDB


class Changes(TMDB):
    """
    Changes functionality.

    See: https://developers.themoviedb.org/3/changes
    """
    BASE_PATH = ''
    URLS = {
        'movie': 'movie/changes',
        'tv': 'tv/changes',
        'person': 'person/changes',
    }

    def movie(self, **kwargs):
        """
        Get a list of all of the movie ids that have been changed
        in the past 24 hours.

        You can query it for up to 14 days worth of changed IDs at
        a time with the start_date and end_date query parameters.
        100 items are returned per page.

        Args:
            start_date: (optional) Expected format is 'YYYY-MM-DD'.
            end_date: (optional) Expected format is 'YYYY-MM-DD'.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('movie')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def tv(self, **kwargs):
        """
        Get a list of all of the TV show ids that have been changed
        in the past 24 hours.

        You can query it for up to 14 days worth of changed IDs at
        a time with the start_date and end_date query parameters.
        100 items are returned per page.

        Args:
            start_date: (optional) Expected format is 'YYYY-MM-DD'.
            end_date: (optional) Expected format is 'YYYY-MM-DD'.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('tv')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def person(self, **kwargs):
        """
        Get a list of all of the person ids that have been changed
        in the past 24 hours.

        You can query it for up to 14 days worth of changed IDs at
        a time with the start_date and end_date query parameters.
        100 items are returned per page.

        Args:
            start_date: (optional) Expected format is 'YYYY-MM-DD'.
            end_date: (optional) Expected format is 'YYYY-MM-DD'.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict respresentation of the JSON returned from the API.
        """
        path = self._get_path('person')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response
