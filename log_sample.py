import logging

import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s::%(name)s:%(levelname)s:%(message)s")
file_handler = logging.FileHandler(filename="sample.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

"""
logging.basicConfig(
    filename="sample.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(name)s:%(levelname)s:%(message)s"
)
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


NUM_1 = 20
NUM_2 = 0

add_result = add(x=NUM_1, y=NUM_2)
logger.debug(f"ADD: {NUM_1} + {NUM_2} = {add_result}")

subtract_result = subtract(x=NUM_1, y=NUM_2)
logger.debug(f"SUBTRACT: {NUM_1} - {NUM_2} = {subtract_result}")

multiply_result = multiply(x=NUM_1, y=NUM_2)
logger.debug(f"MULTIPLY: {NUM_1} * {NUM_2} = {multiply_result}")

divide_result = divide(x=NUM_1, y=NUM_2)
logger.debug(f"DIVIDE: {NUM_1} / {NUM_2} = {divide_result}")