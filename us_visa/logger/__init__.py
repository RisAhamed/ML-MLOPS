
import logging
import os
from datetime import datetime

# Create a logger
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.INFO)

# Create a log folder if it doesn't exist
log_folder = 'logs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Create a log file name with timestamp
log_file_name = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'

# Create a file handler
file_handler = logging.FileHandler(os.path.join(log_folder, log_file_name))

# Create a console handler
console_handler = logging.StreamHandler()

# Set the logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# # Example usage:
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')