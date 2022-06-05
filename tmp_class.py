import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("employee.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


"""
logging.basicConfig(
    filename="employee.log",
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s",
) # ROOT LOGGER
"""


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):

        self.first = first
        self.last = last

        logger.info(f"Created employee: {self.fullname} - {self.email}")

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"


emp1 = Employee(first="John", last="Smith")
emp2 = Employee(first="Pavle", last="Ristovic")
emp3 = Employee(first="Jane", last="Doe")
