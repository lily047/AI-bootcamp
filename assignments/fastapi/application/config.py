import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(): 
    DEBUG = False 
    SQLITE_DB_DIR = None 
    SQLALCHEMY_DATABASE_URI = None

class LocalDevelopmentConfig(BaseConfig): 
    DEBUG = True