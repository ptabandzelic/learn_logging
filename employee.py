import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s::%(name)s:%(levelname)s:%(message)s")
file_handler = logging.FileHandler(filename="employee.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

"""
logging.basicConfig(
    filename="employee.log",
    level=logging.INFO,
    format="%(asctime)s::%(name)s:%(levelname)s:%(message)s"
)
"""

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(f"Created Employee: {self.first} {self.last}")

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"


emp1 = Employee(first="John", last="Great")
emp2 = Employee(first="Pavle", last="Takeshi")
emp3 = Employee(first="Joe", last="Doe")
