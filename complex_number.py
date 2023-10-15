
class ComplexNumber:

    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return f"{self.real} + {self.imaginary}i" if self.imaginary >= 0 else f"{self.real} - {-self.imaginary}i"
