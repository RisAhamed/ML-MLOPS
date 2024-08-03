# custom_exceptions.py

import traceback
import os
import logging
from us_visa.logger import logger
from datetime import datetime

class CustomException(Exception):
    def __init__(self, exception, error_code=500, error_type="ServerError"):
        self.exception = exception
        self.error_code = error_code
        self.error_type = error_type
        self.error_details = self.get_error_details()
        self.log_error()

    def get_error_details(self):
        error_details = {}
        try:
            raise self.exception
        except Exception as e:
            error_details['file_name'] = os.path.basename(traceback.extract_tb(e.__traceback__)[-1].filename)
            error_details['folder_name'] = os.path.dirname(traceback.extract_tb(e.__traceback__)[-1].filename)
            error_details['line_number'] = traceback.extract_tb(e.__traceback__)[-1].lineno
            error_details['script_error'] = str(e)
        return error_details


    def log_error(self):
        log_file_name = f"{self.error_details['file_name']}_{self.error_details['line_number']}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        logging.basicConfig(filename=log_file_name, level=logging.ERROR, format='%(message)s', filemode='w')
        error_message = f"Error Code: {self.error_code}, Error Type: {self.error_type}, Message: {str(self.exception)}, Error Details: {self.error_details}"
        logger.info(error_message)
        print(error_message)  # Print the error message to the cmd

    def __str__(self):
        error_message = f"Error Code: {self.error_code}, Error Type: {self.error_type}, Message: {str(self.exception)}, File Name: {self.error_details['file_name']}, Folder Name: {self.error_details['folder_name']}, Line Number: {self.error_details['line_number']}, Script Error: {self.error_details['script_error']}"
        return error_message

# Example usage:
