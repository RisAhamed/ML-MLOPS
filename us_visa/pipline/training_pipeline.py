# from us_visa.components import data_ingestion
from us_visa.components.data_ingestion import DataIngestion
from us_visa.exception  import CustomException
import sys
from us_visa.logger import logger
from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()


    

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of TrainPipeline class is responsible for starting data ingestion component
        """
        try:
            logger.info("Entered the start_data_ingestion method of TrainPipeline class")
            logger.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logger.info("Got the train_set and test_set from mongodb")
            logger.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )
            return data_ingestion_artifact
        
        except Exception as e:
            raise CustomException (e,sys)
        
    def run_pipeline(self,)->None:
        try:
            logger.info("Entered the run_pipeline method of TrainPipeline class")
            data_ingestion_artifact = self.start_data_ingestion()
            logger.info("Data ingestion completed successfully")
            # Here you can add your other pipeline steps
            # For example, feature engineering, model training, and evaluation
            # ...
            logger.info("Exited the run_pipeline method of TrainPipeline class")

        except Exception as e:
            raise CustomException(e,sys) 