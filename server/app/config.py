import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    #os.environ['DATABASE_URL']

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
