from abc import ABC, abstractmethod
from complex_number import ComplexNumber
from logger_setup import logger


# Interface for ComplexNumberOperations
class ComplexNumberOperations(ABC):

    @abstractmethod
    def execute(self, a, b):
        pass


# Class to implement Addition operation
class ComplexNumberAddition(ComplexNumberOperations):

    def execute(self, a, b):
        result = ComplexNumber(a.real + b.real, a.imaginary + b.imaginary)
        logger.info(f"Adding {a} and {b} results in {result}")
        return result


# Class to implement Multiplication operation
class ComplexNumberMultiplication(ComplexNumberOperations):

    def execute(self, a, b):
        real_part = a.real * b.real - a.imaginary * b.imaginary
        imaginary_part = a.real * b.imaginary + a.imaginary * b.real
        result = ComplexNumber(real_part, imaginary_part)
        logger.info(f"Multiplying {a} and {b} results in {result}")
        return result


# Class to implement Division operation
class ComplexNumberDivision(ComplexNumberOperations):

    def execute(self, a, b):
        if b.real == 0 and b.imaginary == 0:
            logger.error("Cannot divide by zero!")
            raise ValueError("Cannot divide by zero!")

        denom = b.real ** 2 + b.imaginary ** 2
        real_part = (a.real * b.real + a.imaginary * b.imaginary) / denom
        imaginary_part = (a.imaginary * b.real - a.real * b.imaginary) / denom
        result = ComplexNumber(real_part, imaginary_part)
        logger.info(f"Dividing {a} by {b} results in {result}")
        return result
