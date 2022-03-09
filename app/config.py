from distutils.debug import DEBUG


class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    pass
class ProdConfig(Config):
    '''
    production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    developement configuration child class
    '''
    DEBUG = True