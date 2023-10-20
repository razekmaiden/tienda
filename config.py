class Config(object):
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}