# -*- coding: utf-8 -*-

"""
tmdbsimple.watch_providers
~~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Watch Providers functionality of tmdbsimple.

Created by lardbit on 2024-09-02.

:copyright: (c) 2013-2022 by Celia Oakley
:license: GPLv3, see LICENSE for more details
"""

from .base import TMDB


class WatchProviders(TMDB):
    """
    Watch Providers functionality.

    See: https://developer.themoviedb.org/reference/watch-providers-available-regions
    See: https://developer.themoviedb.org/reference/watch-providers-movie-list
    See: https://developer.themoviedb.org/reference/watch-provider-tv-list
    """
    BASE_PATH = 'watch'
    URLS = {
        'watch-providers-available-regions': '/providers/regions',
        'watch-providers-movie-list': '/providers/movie',
        'watch-provider-tv-list': '/providers/tv',
    }

    def watch_providers_available_regions(self, **kwargs):
        """
        Get the list of the countries we have watch provider (OTT/streaming) data for.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path('watch-providers-available-regions')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def watch_providers_movie_list(self, **kwargs):
        """
        Get the list of streaming providers we have for movies.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path('watch-providers-movie-list')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def watch_providers_tv_list(self, **kwargs):
        """
        Get the list of streaming providers we have for tv.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path('watch-provider-tv-list')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response
