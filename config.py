class Config(object):
    SECRET_KEY = '#5tFrZCysP^six53Lc*6'


class DevelopmentConfig(Config):
    DEBUG = True
    DB_CREDENTIALS = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : '',
    'database' : 'tienda'}


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}