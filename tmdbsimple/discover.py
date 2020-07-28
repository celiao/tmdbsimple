# -*- coding: utf-8 -*-

"""
tmdbsimple.discover
~~~~~~~~~~~~~~~~~~~
This module implements the Discover functionality of tmdbsimple.

Created by Celia Oakley on 2013-10-31.

:copyright: (c) 2013-2020 by Celia Oakley
:license: GPLv3, see LICENSE for more details
"""

from .base import TMDB


class Discover(TMDB):
    """
    Discover functionality.

    See: https://developers.themoviedb.org/3/discover
    """
    BASE_PATH = 'discover'
    URLS = {
        'movie': '/movie',
        'tv': '/tv',
    }

    def movie(self, **kwargs):
        """
        Discover movies by different types of data like average rating, number
        of votes, genres and certifications. You can get a valid list of
        certifications from the certifications list method.

        Discover also supports a nice list of sort options. See below for all
        of the available options.

        Please note, when using certification / certification.lte you must also
        specify certification_country. These two parameters work together in
        order to filter the results. You can only filter results with the
        countries we have added to our certifications list.

        If you specify the region parameter, the regional release date will be
        used instead of the primary release date. The date returned will be the
        first date based on your query (ie. if a with_release_type is
        specified). It's important to note the order of the release types that
        are used. Specifying "2|3" would return the limited theatrical release
        date as opposed to "3|2" which would return the theatrical date.

        Also note that a number of filters support being comma (,) or pipe (|)
        separated. Comma's are treated like an AND and query while pipe's are
        an OR.

        Some examples of what can be done with discover can be found at
        https://www.themoviedb.org/documentation/api/discover.

        Args:
            language: (optional) ISO 639-1 code.
            region: (optional) Specify a ISO 3166-1 code.
            sort_by: (optional) Allowed values: popularity.asc,
                popularity.desc, release_date.asc, release_date.desc,
                revenue.asc, revenue.desc, primary_release_date.asc,
                primary_release_date.desc, original_title.asc,
                original_title.desc, vote_average.asc, vote_average.desc,
                vote_count.asc, vote_count.desc
                Default: popularity.desc
            certification_country: (optional) Used in conjunction with the
                certification filter, use this to specify a country with a
                valid certification.
            certification: Filter results with a valid certification from the
                'certification_country' field.
            certification.gte: Filter and only include movies that have a
                certification that is greater than or equal to the specified
                value.
            certification.lte: Filter and only include movies that have a
                certification that is less than or equal to the specified
                value.
            include_adult: (optional) A filter and include or exclude adult
                movies.
            include_video: (optional) A filter to include or exclude videos.
            page: (optional) Minimum 1, maximum 1000, default 1.
            primary_release_year: (optional) A filter to limit the results to a
                specific primary release year.
            primary_release_date.gte: (optional) Filter and only include movies
                that have a primary release date that is greater or equal to
                the specified value.
            primary_release_date.lte: (optional) Filter and only include movies
                that have a primary release date that is less than or equal to
                the specified value.
            release_date.gte: (optional) Filter and only include movies that
                have a primary release date that is greater or equal to the
                specified value.
            releaste_date.lte: (optional) Filter and only include movies that
                have a primary release date that is less than or equal to the
                specified value.
            with_release_type: (optional) Specify a comma (AND) or pipe (OR)
                separated value to filter release types by. These release types
                map to the same values found on the movie release date method.
                Minimum 1, maximum 6.
            year: (optional) A filter to limit the results to a specific year
                (looking at all release dates).
            vote_count.gte: (optional) Filter and only include movies that have
                a vote count that is greater or equal to the specified value.
                Minimum 0.
            vote_count.lte: (optional) Filter and only include movies that have
                a vote count that is less than or equal to the specified value.
                Minimum 1.
            vote_average.gte: (optional) Filter and only include movies that
                have a rating that is greater or equal to the specified value.
                Minimum 0.
            vote_average.lte: (optional) Filter and only include movies that
                have a rating that is less than or equal to the specified value.
                Minimum 0.
            with_cast: (optional) A comma separated list of person ID's. Only
                include movies that have one of the ID's added as an actor. 
            with_crew: (optional) A comma separated list of person ID's. Only
                include movies that have one of the ID's added as a crew member.
            with_people: (optional) A comma separated list of person ID's. Only
                include movies that have one of the ID's added as a either a
                actor or a crew member.
            with_companies: (optional) A comma separated list of production
                company ID's. Only include movies that have one of the ID's
                added as a production company.
            with_genres: (optional) Comma separated value of genre ids that you
                want to include in the results.
            without_genres: (optional) Comma separated value of genre ids that
                you want to exclude from the results.
            with_keywords: (optional) A comma separated list of keyword ID's.
                Only includes movies that have one of the ID's added as a
                keyword.
            without_keywords: (optional) Exclude items with certain keywords.
                You can comma and pipe seperate these values to create an 'AND' or 'OR' logic.
            with_runtime.gte: (optional) Filter and only include movies that
                have a runtime that is greater or equal to a value.
            with_runtime.lte: (optional) Filter and only include movies that
                have a runtime that is less than or equal to a value.
            with_original_language: (optional) Specify an ISO 639-1 string to
                filter results by their original language value.

        Returns:
            A dict respresentation of the JSON returned from the API.
        """
        # Periods are not allowed in keyword arguments but several API
        # arguments contain periods. See both usages in tests/test_discover.py.
        for param in dict(kwargs):
            if '_lte' in param:
                kwargs[param.replace('_lte', '.lte')] = kwargs.pop(param)
            if '_gte' in param:
                kwargs[param.replace('_gte', '.gte')] = kwargs.pop(param)

        path = self._get_path('movie')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def tv(self, **kwargs):
        """
        Discover TV shows by different types of data like average rating,
        number of votes, genres, the network they aired on and air dates.

        Discover also supports a nice list of sort options. See below for all
        of the available options.

        Also note that a number of filters support being comma (,) or pipe (|)
        separated. Comma's are treated like an AND and query while pipe's are
        an OR.

        Some examples of what can be done with discover can be found at
        https://www.themoviedb.org/documentation/api/discover.

        Args:
            page: (optional) Minimum 1, maximum 1000.
            language: (optional) ISO 639-1 code.
            sort_by: (optional) Available options are 'vote_average.desc',
                     'vote_average.asc', 'first_air_date.desc',
                     'first_air_date.asc', 'popularity.desc', 'popularity.asc'
            first_air_year: (optional) Filter the results release dates to
                            matches that include this value. Expected value
                            is a year.
            vote_count.gte or vote_count_gte: (optional) Only include TV shows
                            that are equal to,
                            or have vote count higher than this value. Expected
                            value is an integer.
            vote_average.gte or vote_average_gte: (optional) Only include TV
                              shows that are equal
                              to, or have a higher average rating than this
                              value.  Expected value is a float.
            with_genres: (optional) Only include TV shows with the specified
                         genres. Expected value is an integer (the id of a
                         genre).  Multiple valued can be specified. Comma
                         separated indicates an 'AND' query, while a
                         pipe (|) separated value indicates an 'OR'.
            with_networks: (optional) Filter TV shows to include a specific
                           network. Expected value is an integer (the id of a
                           network).  They can be comma separated to indicate an
                           'AND' query.
            first_air_date.gte or first_air_date_gte: (optional) The minimum
                                release to include.
                                Expected format is 'YYYY-MM-DD'.
            first_air_date.lte or first_air_date_lte: (optional) The maximum
                                release to include.
                                Expected format is 'YYYY-MM-DD'.

        Returns:
            A dict respresentation of the JSON returned from the API.
        """
        # Periods are not allowed in keyword arguments but several API
        # arguments contain periods. See both usages in tests/test_discover.py.
        for param in dict(kwargs):
            if '_lte' in param:
                kwargs[param.replace('_lte', '.lte')] = kwargs.pop(param)
            if '_gte' in param:
                kwargs[param.replace('_gte', '.gte')] = kwargs.pop(param)

        path = self._get_path('tv')

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response
