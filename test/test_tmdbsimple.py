"""
test.py contains unit tests for tmdbsimple.py

Fill in Global Variables below before running tests.

Created by Celia Oakley on 2013-11-05
"""

import unittest
import sys
sys.path.append("../tmdbsimple")

from tmdbsimple import TMDB

#
# Global Variables (fill in or put in keys.py)
#
TMDB_API_KEY = 'YOUR_API_KEY_HERE' 
REQUEST_TOKEN = 'YOUR_REQUEST_TOKEN_HERE'
SESSION_ID = 'YOUR_SESSION_ID_HERE'
USERNAME = 'YOUR_USERNAME_HERE'

try:
    from keys import *
except ImportError:
    pass

LISTNAME = 'Yet Another List of Movies'
MOVIETITLE = 'The Brother From Another Planet'

class ConfigurationCheck(unittest.TestCase):
    def testConfigurationInfo(self):
        change_keys = ['adult', 'also_known_as', 'alternative_titles', \
            'biography', 'birthday', 'budget', 'cast', 'character_names', \
            'crew', 'deathday', 'general', 'genres', 'homepage', 'images', \
            'imdb_id', 'name', 'original_title', 'overview', 'plot_keywords', \
            'production_companies', 'production_countries', 'releases', \
            'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', \
            'title', 'trailers', 'translations']

        tmdb = TMDB(TMDB_API_KEY)
        config = tmdb.Configuration()
        response = config.info()
        self.assertEqual(config.change_keys, change_keys)

        status_code = 7
        tmdb = TMDB(0)
        config = tmdb.Configuration()
        response = config.info()
        self.assertEqual(config.status_code, status_code)

class AccountCheck(unittest.TestCase):
    # run this test with a valid session_id and authenticated account
    # see SESSION_ID and USERNAME above
    def testAccountInfo(self):
        username = USERNAME
        tmdb = TMDB(TMDB_API_KEY)
        acct = tmdb.Account(SESSION_ID)
        response = acct.info()
        self.assertEqual(acct.username, username)

    def testAccountLists(self):
        tmdb = TMDB(TMDB_API_KEY)
        acct = tmdb.Account(SESSION_ID)
        response = acct.lists()
        self.assertTrue(hasattr(acct, 'results'))

    def testAccountFavoriteMovies(self):
        movietitle = MOVIETITLE
        tmdb = TMDB(TMDB_API_KEY)
        acct = tmdb.Account(SESSION_ID)
        response = acct.favorite_movies()
        self.assertEqual(acct.results[0]['title'], movietitle)

    def testAccountFavorite(self):
        params = {'movie_id': 62211, 'favorite': True}
        status_code = 12 # updated successfully
        tmdb = TMDB(TMDB_API_KEY)
        acct = tmdb.Account(SESSION_ID)
        response = acct.info() # to set acct.id
        response = acct.favorite(params)
        self.assertEqual(acct.status_code, status_code)

    def testAccountRatedMovies(self):
        tmdb = TMDB(TMDB_API_KEY)
        acct = tmdb.Account(SESSION_ID)
        response = acct.info() # to set acct.id
        response = acct.rated_movies({'page': 1, 'sort_by': 'created_at'})
        self.assertTrue(hasattr(acct, 'results'))

    def testAccountWatchList(self):
        movietitle = MOVIETITLE
        tmdb = TMDB(TMDB_API_KEY)
        acct = tmdb.Account(SESSION_ID)
        response = acct.info() # to set acct.id
        response = acct.movie_watchlist({'page': 1, 'sort_by': 'created_at'})
        self.assertEqual(acct.results[0]['title'], movietitle)

    def testAccountWatchListPost(self):
        params = {'movie_id': 11, 'movie_watchlist': True}
        status_code = 12 # updated successfully
        tmdb = TMDB(TMDB_API_KEY)
        acct = tmdb.Account(SESSION_ID)
        response = acct.info() # to set acct.id
        response = acct.movie_watchlist_post(params)
        self.assertEqual(acct.status_code, status_code)

class AuthenticationCheck(unittest.TestCase):
    def testAuthenticationTokenNew(self):
        success = True
        tmdb = TMDB(TMDB_API_KEY)
        auth = tmdb.Authentication()
        response = auth.token_new()
        self.assertEqual(auth.success, success)

    # run this test with a valid, one-time-use request_token
    # see REQUEST_TOKEN above
    def testAuthenticationSessionNew(self):
        params = {'request_token': 'REQUEST_TOKEN'}
        success = True
        tmdb = TMDB(TMDB_API_KEY)
        auth = tmdb.Authentication()
        response = auth.session_new(params)
        #print(auth.session_id)
        self.assertEqual(auth.success, success)

    def testAuthenticationGuestSessionNew(self):
        success = True
        tmdb = TMDB(TMDB_API_KEY)
        auth = tmdb.Authentication()
        response = auth.guest_session_new()
        #print(auth.guest_session_id)
        self.assertEqual(auth.success, success)

class ChangesCheck(unittest.TestCase):
    def testChangesMovie(self):
        tmdb = TMDB(TMDB_API_KEY)
        changes = tmdb.Changes()
        response = changes.movie()
        self.assertTrue(hasattr(changes, 'results'))

    def testChangesPerson(self):
        tmdb = TMDB(TMDB_API_KEY)
        change = tmdb.Changes()
        response = change.movie()
        self.assertTrue(hasattr(change, 'results'))

class CollectionsCheck(unittest.TestCase):
    def testCollectionsInfo(self):
        id = 10
        name = 'Star Wars Collection'
        tmdb = TMDB(TMDB_API_KEY)
        collection = tmdb.Collections(id)
        response = collection.info()
        self.assertEqual(collection.name, name)

    def testCollectionsImages(self):
        id = 10
        tmdb = TMDB(TMDB_API_KEY)
        collection = tmdb.Collections(id)
        response = collection.images()
        self.assertTrue(hasattr(collection, 'backdrops'))

class CompaniesCheck(unittest.TestCase):
    def testCompaniesInfo(self):
        id = 1
        name = 'Lucasfilm'
        tmdb = TMDB(TMDB_API_KEY)
        company = tmdb.Companies(id)
        response = company.info()
        self.assertEqual(company.name, name)

    def testCompaniesMovies(self):
        id = 1
        tmdb = TMDB(TMDB_API_KEY)
        company = tmdb.Companies(id)
        response = company.movies()
        self.assertTrue(hasattr(company, 'results'))

class CreditsCheck(unittest.TestCase):
    def testCreditsInfo(self):
        id = '52542282760ee313280017f9'
        department = 'Actors'
        tmdb = TMDB(TMDB_API_KEY)
        credit = tmdb.Credits(id)
        response = credit.info()
        self.assertEqual(credit.department, department)

class DiscoverCheck(unittest.TestCase):
    def testDiscoverMovie(self):
        tmdb = TMDB(TMDB_API_KEY)
        discover = tmdb.Discover()
        response = discover.movie({'page': 1, 'year': '2004'})
        self.assertTrue(hasattr(discover, 'results'))

    def testDiscoverTV(self):
        tmdb = TMDB(TMDB_API_KEY)
        discover = tmdb.Discover()
        response = discover.tv({'page':2, 'vote_average.gte': 5})
        self.assertTrue(hasattr(discover, 'results'))

class FindCheck(unittest.TestCase):
    def testFindInfo(self):
        id = 'tt0266543'
        external_source = 'imdb_id'
        title = 'Finding Nemo'
        tmdb = TMDB(TMDB_API_KEY)
        find = tmdb.Find(id)
        response = find.info({'external_source': external_source})
        self.assertEqual(find.movie_results[0]['title'], title)

class GenresCheck(unittest.TestCase):
    def testGenresList(self):
        tmdb = TMDB(TMDB_API_KEY)
        genre = tmdb.Genres()
        response = genre.list()
        self.assertTrue(hasattr(genre, 'genres'))

    def testGenresMovies(self):
        id = 18
        tmdb = TMDB(TMDB_API_KEY)
        genre = tmdb.Genres(id)
        response = genre.movies()
        self.assertTrue(hasattr(genre, 'results'))

class JobsCheck(unittest.TestCase):
    def testJobsList(self):
        tmdb = TMDB(TMDB_API_KEY)
        lst = tmdb.Jobs()
        response = lst.list()
        self.assertTrue(hasattr(lst, 'jobs'))

class KeywordsCheck(unittest.TestCase):
    def testKeywordsInfo(self):
        id = 1721
        name = 'fight'
        tmdb = TMDB(TMDB_API_KEY)
        keyword = tmdb.Keywords(id)
        response = keyword.info()
        self.assertEqual(keyword.name, name)

    def testKeywordsMovies(self):
        id = 1721
        tmdb = TMDB(TMDB_API_KEY)
        keyword = tmdb.Keywords(id)
        response = keyword.movies()
        self.assertTrue(hasattr(keyword, 'results'))

class ListsCheck(unittest.TestCase):
    def testListsInfo(self):
        id = '509ec17b19c2950a0600050d'
        created_by = 'Travis Bell'
        tmdb = TMDB(TMDB_API_KEY)
        lst = tmdb.Lists(id)
        response = lst.info()
        self.assertEqual(lst.created_by, created_by)

    def testListsItemStatus(self):
        id = '509ec17b19c2950a0600050d'
        movie_id = 74643
        tmdb = TMDB(TMDB_API_KEY)
        lst = tmdb.Lists(id)
        response = lst.item_status({'movie_id': movie_id})
        self.assertTrue(hasattr(lst, 'item_present'))

    def testListsCreateAddItemRemoveItemDeleteList(self):
        status_message = 'Success'
        tmdb = TMDB(TMDB_API_KEY)
        lst = tmdb.Lists(0, SESSION_ID)
        response = lst.create_list({'name': 'My awesome list', \
                                    'description': 'No duplicates here'})
        self.assertEqual(lst.status_message, status_message)

        list_id = lst.list_id

        status_code = 12 # Success
        lst = tmdb.Lists(list_id, SESSION_ID)
        response = lst.add_item({'media_id': 550})
        self.assertEqual(lst.status_code, status_code)

        status_code = 13 # Success
        tmdb = TMDB(TMDB_API_KEY)
        lst = tmdb.Lists(list_id, SESSION_ID)
        response = lst.remove_item({'media_id': 550})
        self.assertEqual(lst.status_code, status_code)

        status_code = 13 # Success
        tmdb = TMDB(TMDB_API_KEY)
        lst = tmdb.Lists(list_id, SESSION_ID)
        response = lst.delete_list()
        self.assertEqual(lst.status_code, status_code)

class MoviesCheck(unittest.TestCase):
    def testMoviesInfo(self):
        id = 103332
        title = 'Ruby Sparks'
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.info()
        self.assertEqual(movie.title, title)

    def testMoviesInfoWithParams(self):
        id = 103332
        title = "Elle s'appelle Ruby"
        params = {'language': 'fr'}
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.info(params)
        self.assertEqual(movie.title, title)

    def testMoviesAlternativeTitles(self):
        id = 550
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.alternative_titles()
        self.assertTrue(hasattr(movie, 'titles'))

    def testMoviesCredits(self):
        id = 103332
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.credits()
        self.assertTrue(hasattr(movie, 'cast'))

    def testMoviesImages(self):
        id = 103332
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.images()
        self.assertTrue(hasattr(movie, 'backdrops'))

    def testMoviesKeywords(self):
        id = 103332
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.keywords()
        self.assertTrue(hasattr(movie, 'keywords'))

    def testMoviesReleases(self):
        id = 103332
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.releases()
        self.assertTrue(hasattr(movie, 'countries'))

    def testMoviesTrailers(self):
        id = 103332
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.trailers()
        self.assertTrue(hasattr(movie, 'youtube'))

    def testMoviesTranslations(self):
        id = 550
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.translations()
        self.assertTrue(hasattr(movie, 'translations'))

    def testMoviesSimilarMovies(self):
        id = 550
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.similar_movies()
        self.assertTrue(hasattr(movie, 'results'))

    def testMoviesReviews(self):
        id = 49026
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.reviews()
        self.assertTrue(hasattr(movie, 'results'))

    def testMoviesLists(self):
        id = 103332
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.lists()
        self.assertTrue(hasattr(movie, 'results'))

    def testMoviesChanges(self):
        id = 103332
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.changes()
        self.assertTrue(hasattr(movie, 'changes'))

    def testMoviesLatest(self):
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies()
        response = movie.latest()
        self.assertTrue(hasattr(movie, 'popularity'))

    def testMoviesUpcoming(self):
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies()
        response = movie.upcoming()
        self.assertTrue(hasattr(movie, 'results'))

    def testMoviesNowPlaying(self):
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies()
        response = movie.now_playing()
        self.assertTrue(hasattr(movie, 'results'))

    def testMoviesPopular(self):
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies()
        response = movie.popular()
        self.assertTrue(hasattr(movie, 'results'))

    def testMoviesTopRated(self):
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies()
        response = movie.top_rated()
        self.assertTrue(hasattr(movie, 'results'))

    def testMoviesAccountStates(self):
        id = 550
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.account_states({'session_id': SESSION_ID})
        self.assertTrue(hasattr(movie, 'favorite'))

    def testMoviesRating(self):
        id = 103332
        status_code = 12 # Success
        tmdb = TMDB(TMDB_API_KEY)
        movie = tmdb.Movies(id)
        response = movie.rating({'session_id': SESSION_ID}, {'value': 7.5})
        self.assertEqual(movie.status_code, status_code)

class NetworksCheck(unittest.TestCase):
    def testNetworksInfo(self):
        id = 49
        name = 'HBO'
        tmdb = TMDB(TMDB_API_KEY)
        network = tmdb.Networks(id)
        response = network.info()
        self.assertEqual(network.name, name)

class PeopleCheck(unittest.TestCase):
    def testPeopleInfo(self):
        id = 287
        name = 'Brad Pitt'
        tmdb = TMDB(TMDB_API_KEY)
        person = tmdb.People(id)
        response = person.info()
        self.assertEqual(person.name, name)

    def testPeopleMovieCredits(self):
        id = 287
        tmdb = TMDB(TMDB_API_KEY)
        person = tmdb.People(id)
        response = person.movie_credits()
        self.assertTrue(hasattr(person, 'cast'))

    def testPeopleTVCredits(self):
        id = 287
        tmdb = TMDB(TMDB_API_KEY)
        person = tmdb.People(id)
        response = person.tv_credits()
        self.assertTrue(hasattr(person, 'cast'))

    def testPeopleCombinedCredits(self):
        id = 287
        tmdb = TMDB(TMDB_API_KEY)
        person = tmdb.People(id)
        response = person.combined_credits()
        self.assertTrue(hasattr(person, 'cast'))

    def testPeopleImages(self):
        id = 287
        tmdb = TMDB(TMDB_API_KEY)
        person = tmdb.People(id)
        response = person.images()
        self.assertTrue(hasattr(person, 'profiles'))

    def testPeopleChanges(self):
        id = 287
        tmdb = TMDB(TMDB_API_KEY)
        person = tmdb.People(id)
        response = person.changes()
        self.assertTrue(hasattr(person, 'changes'))

    def testPeoplePopular(self):
        tmdb = TMDB(TMDB_API_KEY)
        person = tmdb.People()
        response = person.popular()
        self.assertTrue(hasattr(person, 'results'))

    def testPeopleLatest(self):
        tmdb = TMDB(TMDB_API_KEY)
        person = tmdb.People()
        response = person.latest()
        self.assertTrue(hasattr(person, 'birthday'))

class ReviewsCheck(unittest.TestCase):
    def testReviewsInfo(self):
        id = '5013bc76760ee372cb00253e' 
        author = 'Chris'
        tmdb = TMDB(TMDB_API_KEY)
        review = tmdb.Reviews(id)
        response = review.info()
        self.assertEqual(review.author, author)

class SearchCheck(unittest.TestCase):
    def testSearchMovie(self):
        query = 'Club'
        tmdb = TMDB(TMDB_API_KEY)
        search = tmdb.Search()
        response = search.movie({'query': query})
        self.assertTrue(hasattr(search, 'results'))

    def testSearchCollection(self):
        query = 'Avenger'
        tmdb = TMDB(TMDB_API_KEY)
        search = tmdb.Search()
        response = search.collection({'query': query})
        self.assertTrue(hasattr(search, 'results'))

    def testSearchTV(self):
        query = 'Breaking'
        tmdb = TMDB(TMDB_API_KEY)
        search = tmdb.Search()
        response = search.tv({'query': query})
        self.assertTrue(hasattr(search, 'results'))

    def testSearchPerson(self):
        query = 'Brad Pitt'
        tmdb = TMDB(TMDB_API_KEY)
        search = tmdb.Search()
        response = search.person({'query': query})
        self.assertTrue(hasattr(search, 'results'))

    def testSearchList(self):
        query = 'Oscars'
        tmdb = TMDB(TMDB_API_KEY)
        search = tmdb.Search()
        response = search.list({'query': query})
        self.assertTrue(hasattr(search, 'results'))

    def testSearchCompany(self):
        query = 'Sony Pictures'
        tmdb = TMDB(TMDB_API_KEY)
        search = tmdb.Search()
        response = search.company({'query': query})
        self.assertTrue(hasattr(search, 'results'))

    def testSearchKeyword(self):
        query = 'fight'
        tmdb = TMDB(TMDB_API_KEY)
        search = tmdb.Search()
        response = search.keyword({'query': query})
        self.assertTrue(hasattr(search, 'results'))

class TVCheck(unittest.TestCase):
    def testTVInfo(self):
        id = 1396
        name = 'Breaking Bad'
        tmdb = TMDB(TMDB_API_KEY)
        tv = tmdb.TV(id)
        response = tv.info()
        self.assertEqual(tv.name, name)

    def testTVCredits(self):
        id = 1396
        tmdb = TMDB(TMDB_API_KEY)
        tv = tmdb.TV(id)
        response = tv.credits()
        self.assertTrue(hasattr(tv, 'cast'))

    def testTVExternalIds(self):
        id = 1396
        imdb_id = 'tt0903747'
        tmdb = TMDB(TMDB_API_KEY)
        tv = tmdb.TV(id)
        response = tv.external_ids()
        self.assertEqual(tv.imdb_id, imdb_id)

    def testTVImages(self):
        id = 1396
        tmdb = TMDB(TMDB_API_KEY)
        tv = tmdb.TV(id)
        response = tv.images()
        self.assertTrue(hasattr(tv, 'backdrops'))

    def testTVTranslations(self):
        id = 1396
        tmdb = TMDB(TMDB_API_KEY)
        tv = tmdb.TV(id)
        response = tv.translations()
        self.assertTrue(hasattr(tv, 'translations'))

    def testTVTopRated(self):
        tmdb = TMDB(TMDB_API_KEY)
        tv = tmdb.TV()
        response = tv.top_rated()
        self.assertTrue(hasattr(tv, 'results'))

    def testTVPopular(self):
        tmdb = TMDB(TMDB_API_KEY)
        tv = tmdb.TV()
        response = tv.popular()
        self.assertTrue(hasattr(tv, 'results'))

class TVSeasonsCheck(unittest.TestCase):
    def testTVSeasonsInfo(self):
        id = 3572
        season_number = 1
        name = 'Season 1'
        tmdb = TMDB(TMDB_API_KEY)
        tv_seasons = tmdb.TV_Seasons(id, season_number)
        response = tv_seasons.info()
        self.assertEqual(tv_seasons.name, name)

    def testTVSeasonsCredits(self):
        id = 3572
        season_number = 1
        tmdb = TMDB(TMDB_API_KEY)
        tv_seasons = tmdb.TV_Seasons(id, season_number)
        response = tv_seasons.credits()
        self.assertTrue(hasattr(tv_seasons, 'crew'))

    def testTVSeasonsExternalIds(self):
        id = 3572
        season_number = 1
        tvdb_id = 2547
        tmdb = TMDB(TMDB_API_KEY)
        tv_seasons = tmdb.TV_Seasons(id, season_number)
        response = tv_seasons.external_ids()
        self.assertEqual(tv_seasons.tvdb_id, tvdb_id)

    def testTVSeasonsImages(self):
        id = 3572
        season_number = 1
        tmdb = TMDB(TMDB_API_KEY)
        tv_seasons = tmdb.TV_Seasons(id, season_number)
        response = tv_seasons.images()
        self.assertTrue(hasattr(tv_seasons, 'posters'))

class TVEpisodesCheck(unittest.TestCase):
    def testTVEpisodesInfo(self):
        id = 1396
        season_number = 1
        episode_number = 1
        name = 'Pilot'
        tmdb = TMDB(TMDB_API_KEY)
        tv_episodes = tmdb.TV_Episodes(id, season_number, episode_number)
        response = tv_episodes.info()
        self.assertEqual(tv_episodes.name, name)

    def testTVEpisodesCredits(self):
        id = 1396
        season_number = 1
        episode_number = 1
        tmdb = TMDB(TMDB_API_KEY)
        tv_episodes = tmdb.TV_Episodes(id, season_number, episode_number)
        response = tv_episodes.credits()
        self.assertTrue(hasattr(tv_episodes, 'guest_stars'))

    def testTVEpisodesExternalIds(self):
        id = 1396
        season_number = 1
        episode_number = 1
        imdb_id = 'tt0959621'
        tmdb = TMDB(TMDB_API_KEY)
        tv_episodes = tmdb.TV_Episodes(id, season_number, episode_number)
        response = tv_episodes.external_ids()
        self.assertEqual(tv_episodes.imdb_id, imdb_id)

    def testTVEpisodesImages(self):
        id = 1396
        season_number = 1
        episode_number = 1
        tmdb = TMDB(TMDB_API_KEY)
        tv_episodes = tmdb.TV_Episodes(id, season_number, episode_number)
        response = tv_episodes.images()
        self.assertTrue(hasattr(tv_episodes, 'stills'))

if __name__ == "__main__":
    unittest.main()

# Run with:
#   python3 test_tmdbsimple.py ConfigurationCheck -v
#   python3 test_tmdbsimple.py ConfigurationCheck
#   ... or other Check classes
#   python3 test_tmdbsimple.py -v
#   python3 test_tmdbsimple.psy
