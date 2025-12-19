import os

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-is-a-secret-key'

class TestingConfig(Config):
    TESTING = True
    DEBUG = True