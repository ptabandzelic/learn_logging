import logging

import tmp_class

"""
LOGGING LEVELS

1.DEBUG:
Detailed information, typically of interest only when diagnosing problems.

2.INFO
Confirmation that things are working as expected

3.WARNING
An indication that something unexpected happend, or indicative of some problems
 in the near future.The software is still working.

4.ERROR
Due to a more serios problem, the software has not been able to perform some functions

5.CRITICAL
A serious error, indicating that a the problem itself may be unable to continue running

5.INFO
Confirmation that things are working as expected


Default level to LOGGING is set to WARNING.By default it will LOG
WARNING, ERROR, CRITICAL.Its gona ignore DEBUG and INFO statements.

MESSAGE TO CONSOLE

LOGGING_LEVEL:ROOT:MESSAGE
"""

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")

file_handler = logging.FileHandler("sample.log")
file_handler.setLevel(level=logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

"""
logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
) # change logging level
"""

def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception("Tried to divide by zero")
    else:
        return result

num_1 = 10
num_2 = 0

add_result = add(num_1, num_2)
logger.debug(f"Add: {num_1} + {num_2} = {add_result}")

sub_result = subtract(num_1, num_2)
logger.debug(f"Sub: {num_1} - {num_2} = {sub_result}")

multi_result = multiply(num_1, num_2)
logger.debug(f"Multi: {num_1} * {num_2} = {multi_result}")

divide_result = divide(num_1, num_2)
logger.debug(f"Divide: {num_1} / {num_2} = {divide_result}")

