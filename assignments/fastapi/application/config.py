import os 
from sqlalchemy.orm import declarative_base, create_engine, sessionmaker
from models.base import Base 

engine = create_engine("sqlite:///test.sqlite3")

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

db_path = os.path.abspath(os.path.join("./database", 'test.sqlite3'))
print(db_path)


class BaseConfig(): 
    DEBUG = False 
    SQLITE_DB_DIR = None 
    SQLALCHEMY_DATABASE_URI = None
    engine = None 

class LocalDevelopmentConfig(BaseConfig): 
    DEBUG = True
    SQLITE_DB_DIR = os.path.join(basedir, db_path)
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLITE_DB_DIR}'
    engine = 

class TestingConfig(BaseConfig): 
    DEBUG = True 
    SQLITE_DB_DIR = os.path.join(basedir, db_path)
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLITE_DB_DIR}'