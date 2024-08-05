import sys
from us_visa.logger import logger
from us_visa.exception import CustomException
import pymongo
import certifi
from us_visa.exception import CustomException
from us_visa.logger import logger

import os
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY

# mongo_db_url = os.getenv('MONGO_DB_URL')
ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = MONGODB_URL_KEY
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logger.info("MongoDB connection succesfull in mongodb_connection")
        except Exception as e:
            raise CustomException(e,sys)