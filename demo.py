from us_visa.logger import logger
from us_visa.exception import CustomException 

# Example usage:

try:
    a = 1.32/00
    # Your code here
    raise TypeError("int object is not iterable")
except Exception as e:
    CustomException(e)

