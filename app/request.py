from app import app
import urllib.request,json
from .models import movie

Movie = movie.Movie

#getting api key

api_key = app.config['MOVIE_API_KEY']

#getting the movie base url

base_url = app.config['MOVIE_API_BASE_URL']

def get_movies(category):
    '''
    function that gets the json response to out url requests
    '''
    get_movie_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_movie_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results

def process_results(movie_list):
    '''
    function that processes the movie result and transform them to a list of objects
movie_list: a list of dictionaries that contains movie details

rerurns; 
movie_results : a list of movie objects
    '''
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results

def get_movie(id):
    get_movie_detail_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_detail_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object
