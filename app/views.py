from flask import  render_template
from app import app
from .request import get_movies,get_movie

#views
@app.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''
    #getting popular movies
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')
    title = "Home - Welcome to the best movie review website online"
    return render_template('index.html', title = title, popular = popular_movies, upcoming =upcoming_movies, now_showing = now_showing_movies)

@app.route('/movie/<int:id>')
def movie(id):
    '''
    view movie page that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title= f'{movie.title}'
    return render_template('movie.html',title = title, movie=movie)