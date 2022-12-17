from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    SECRET_KEY = 'Pablo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///recipe.db'
    DEBUG = True
    

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///recipe.db'
    DEBUG = True

class GithubCIConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///recipe.db'
    DEBUG = True
