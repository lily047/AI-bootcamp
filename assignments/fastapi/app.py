from fastapi import FastAPI 
import os 
from application.config import LocalDevelopmentConfig

def create_app(): 

    app = FastAPI()

    env = os.getenv("ENV", "development")

    if env=="production": 
        app.logger.info("Currently no production environment is setup")
        raise Exception("No production server is setup")
    elif env == "testing": 
        app.logger.info("Currently no testing environment is setup")
        raise Exception("No production server is setup")
    else: 
        app.logger.info("Starting local development")
        app.config.from_object(LocalDevelopmentConfig)