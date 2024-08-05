from us_visa.logger  import logger
from us_visa.exception import CustomException
from us_visa.constants  import DATABASE_NAME
from us_visa.configuration.mongodb_connection import MongoDBClient
import pandas as pd
import numpy as np
import sys

class VisaData:
    def __init__(self):
        self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)

    def export_collection_as_dataframe(self, collection_name: str) :
        try:
            # Get the database object
            database = self.mongo_client.database

            # Get the collection object
            collection = database[collection_name]

            # Retrieve the data from the collection
            data = collection.find()

            # Convert the data to a pandas DataFrame
        

            df = pd.DataFrame(data)
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df


        except Exception as e:
            # Log the error message
            logger.error(f"Error exporting {collection_name} collection as a DataFrame: {str(e)}")

            # Raise a custom exception
            raise CustomException(e,sys)
    #USvisaData: