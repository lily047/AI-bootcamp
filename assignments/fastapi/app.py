from fastapi import FastAPI 
import os, logging 
from application.config import LocalDevelopmentConfig, TestingConfig
from application.database import db 

logging.basicConfig(filename='debug.log')

def create_app(): 

    app = FastAPI()

    env = os.getenv("ENV", "development")

    if env=="production": 
        app.logger.info("Currently no production environment is setup")
        raise Exception("No production server is setup")
    elif env == "testing": 
        app.logger.info("Currently no testing environment is setup")
        app.config.from_object(TestingConfig)
    else: 
        app.logger.info("Starting local development")
        app.config.from_object(LocalDevelopmentConfig)