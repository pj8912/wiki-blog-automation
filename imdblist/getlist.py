from imdb import Cinemagoer

movie_list = []

def get_movie_list():
    ia  = Cinemagoer()
    movies = ia.get_top250_movies()
    movie_list = [movies[i]['title'] for i in range(len(movies))]
    # for i in range(len(movies)):
    #     movie_list.append(movies[i]['title'])
    return movie_list