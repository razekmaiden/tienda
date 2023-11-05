from decouple import config

class Config(object):
    SECRET_KEY = '#5tFrZCysP^six53Lc*6'


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 # Puerto que ocupa google para TLS (Transport Layer Security)
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'depto1801tp@gmail.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD')
    DB_CREDENTIALS = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : '',
    'database' : 'tienda'}


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}