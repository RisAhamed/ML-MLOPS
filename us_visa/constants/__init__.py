import os
from datetime import date

DATABASE_NAME = "US_VISA"

COLLECTION_NAME = "VISA_DATA"
from dotenv import load_dotenv
load_dotenv()
# MONGODB_URL_KEY = 'mongodb+srv://Riswan:Riswan@us-visa-cluster.dffpbxg.mongodb.net/?retryWrites=true&w=majority&appName=us-visa-cluster'
# # os.environ[MONGODB_URL_KEY] = MONGODB_URL_KEY
MONGODB_URL_KEY = os.getenv("MONGODB_URL")
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

PIPELINE_NAME :str = 'usvisa'
ARTIFACT_DIR:str = 'artifact'

MODEL_FILE_NAME = "model.pkl"
FILE_NAME:str = 'usvisa.csv'

DATA_INGESTION_COLLECTION_NAME = "visa_data"
DATA_INGESTION_DIR_NAME: str= 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR :str = "feature_store"
DATA_INGESTION_INGESTED_DIR:str ='ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2