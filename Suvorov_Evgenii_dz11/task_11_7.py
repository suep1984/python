class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag > 0:
            return f'{self.real}+{self.imag}i'
        else:
            return f'{self.real}{self.imag}i'

    def __add__(self, other):
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return ComplexNumber(new_real, new_imag)

    def __mul__(self, other):
        new_real = self.real * other.real + -(self.imag * other.imag)
        new_imag = self.imag * other.real + self.real * other.imag
        return ComplexNumber(new_real, new_imag)


a = ComplexNumber(5, -2)
b = ComplexNumber(3, -4)
d = ComplexNumber(1, -1)
e = ComplexNumber(3, 6)

print(a + b)
print(d * e)
