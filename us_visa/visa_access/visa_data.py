from us_visa.logger  import logger
from us_visa.exception import CustomException
from us_visa.constants  import DATABASE_NAME

from us_visa.configuration.mongodb_connection import MongoDBClient
import certifi
import pandas as pd
import numpy as np
import sys
class VisaData:
    def __init__(self):
        self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)

    def export_collection_as_dataframe(self, collection_name: str) -> pd.DataFrame:
        try:
            # Get the database object
            database = self.mongo_client.database

            # Get the collection object
            collection = database[collection_name]

            # Retrieve the data from the collection
            data = collection.find()

            # Convert the data to a pandas DataFrame
            dataframe = pd.DataFrame(list(data))

            # Remove the '_id' and 'case_id' columns
            dataframe.drop(columns = ['_id'], axis=1, inplace=True)
            dataframe.replace({"na":np.nan},inplace=True)
            # Log a success message
            logger.info(f"Successfully exported {collection_name} collection as a DataFrame.")

            return dataframe

        except Exception as e:
            # Log the error message
            logger.error(f"Error exporting {collection_name} collection as a DataFrame: {str(e)}")

            # Raise a custom exception
            raise CustomException(e,sys)