import os
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.exception import CustomException
from us_visa.logger import logger
from us_visa.visa_access.visa_data import  VisaData


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig= DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise CustomException(e)
        
    def export_data_into_feature_store(self)->DataFrame:
     
        """
            Method Name :   export_data_into_feature_store
            Description :   This method exports data from mongodb to csv file
            
            Output      :   data is returned as artifact of data ingestion components
            On Failure  :   Write an exception log and then raise an exception
            """
                    
        try: 
            logger.info("Exporting the data from the mongodb")
            visadata = VisaData()
            dataframe = visadata.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            logger.info( f"exported_collection_as_dataframe with Shape of dataframe: {dataframe.shape} ")

            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logger.info(f"saving the exported data into feature store file path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path, index=False,header = True)
            return dataframe
        
        except Exception as e:
            raise CustomException(e)
        
    def split_data_as_train_test(self,dataframe: DataFrame)->None:
        """
        Method Name :   split_data_as_train_test
        Description :   This method splits the dataframe into train set and test set based on split ratio 
        
        Output      :   Folder is created in s3 bucket
        On Failure  :   Write an exception log and then raise an exception
        """
        logger.info("Entered into train test split of the data ingestion cofig")
        try:
            train_set,test_set = train_test_split(dataframe,test_size = self.data_ingestion_config.train_test_split_ratio)
            # logger.info("Train test split completed")
            logger.info('''train test split of data ingestion completion and now  started into 
                    creating directories''')
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logger.info(f"Exporting the train test split from the data ingestion file into {dir_path}")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index = False,header =True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index =False,header= True)
            logger.info(f"completed  exporting  the train and test into the folders-- {dir_path}")


        except Exception as e:
            raise CustomException(e)
        

    def initiate_data_ingestion(self)->DataIngestionArtifact:

        """
        Method Name :   initiate_data_ingestion
        Description :   This method initiates the data ingestion components of training pipeline 
        
        Output      :   train set and test set are returned as the artifacts of data ingestion components
        On Failure  :   Write an exception log and then raise an exception
        """

        logger.info("enterd into data_ingestion_method of data ingestion class")
        try:
            dataframe = self.export_data_into_feature_store()
            logger.info("Got the data from the mongo db ")
            self.split_data_as_train_test(dataframe)
            logger.info("completed --- train test split on the dataset ")

            logger.info(
                "Exited initiate_data_ingestion method of Data_Ingestion class"
            )
            data_ingestion_artifacts = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                         test_file_path= self.data_ingestion_config.testing_file_path )


        except Exception as e:
            raise CustomException(e) from e
        
    