# import sys
# import os 
# from us_visa.logger  import logger

# from us_visa.exception import CustomException
# import sys

# import os
from us_visa.constants import DATABASE_NAME,MONGODB_URL_KEY
# import pymongo
# import certifi

# ca = certifi.where()

# class MongoDBClient:
#     """
#     Class Name :   MongoDBClient
#     Description :   This class is used to connect to the MongoDB database.
    
#     Output      :   connection to mongodb database
#     On Failure  :   raises an exception
#     """
#     client = None

#     def __init__(self, database_name=DATABASE_NAME) -> None:
#         try:
#             if MongoDBClient.client is None:
#                 mongo_db_url =MONGODB_URL_KEY
#                 if mongo_db_url is None:
#                     raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
#                 MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
#             self.client = MongoDBClient.client
#             self.database = self.client[database_name]
#             self.database_name = database_name
#             logger.info("MongoDB connection successful")
#         except Exception as e:
#             raise CustomException(e, sys)


import sys
import os
from us_visa.logger import logger
from us_visa.exception import CustomException
import pymongo
import certifi
import ssl
import socket

ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   MongoDBClient
    Description :   This class is used to connect to the MongoDB database.
    
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
                
                # Create an SSL context with certificate verification
                context = ssl.create_default_context()
                context.check_hostname = True
                context.verify_mode = ssl.CERT_REQUIRED
                
                # Verify the certificate
                try:
                    with socket.create_connection((mongo_db_url, 27017)) as sock:
                        with context.wrap_socket(sock, server_hostname=mongo_db_url) as ssock:
                            print("Certificate verified successfully")
                except ssl.SSLError as e:
                    raise CustomException(f"Certificate verification failed: {e}", sys)
                
                # Establish the MongoDB connection with SSL/TLS
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca, ssl=True, ssl_cert_reqs=ssl.CERT_REQUIRED)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logger.info("MongoDB connection successful")
        except Exception as e:
            raise CustomException(e, sys)