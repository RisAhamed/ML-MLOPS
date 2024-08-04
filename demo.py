from us_visa.logger import logger
from us_visa.exception import CustomException 
from us_visa.pipline.training_pipeline import TrainingPipeline
from us_visa.constants import DATABASE_NAME,MONGODB_URL_KEY

print(MONGODB_URL_KEY)
print(type(MONGODB_URL_KEY))

obj = TrainingPipeline()
obj.run_pipeline()


