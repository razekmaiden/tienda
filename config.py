class Config(object):
    SECRET_KEY = '#5tFrZCysP^six53Lc*6'

class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}