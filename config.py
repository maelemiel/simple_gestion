import os

class Config:
    DATABASE = os.path.join(os.path.dirname(__file__), 'database.db')
    DEBUG = True