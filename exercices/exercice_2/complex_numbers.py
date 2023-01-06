import math


class Complejo:
    def __init__(self, real, imag):
        self.real = float(real).__round__(2)
        self.imag = float(imag).__round__(2)

    def __add__(self, other):
        return Complejo(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complejo(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complejo(self.real * other.real - self.imag * other.imag,
                        self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        return Complejo((self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2),
                        (self.imag * other.real - self.real * other.imag) / (other.real ** 2 + other.imag ** 2))

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def mod(self):
        mod = math.sqrt(self.real ** 2 + self.imag ** 2)
        return Complejo(mod, 0)

    def __repr__(self):
        return f"Complejo({self.real}, {self.imag})"


A = Complejo(2, 1)
B = Complejo(5, 6)
print("A+B", A + B)
print("A-B", A - B)
print("A*B", A * B)
print("A/B", A / B)
print("Mod(A)", A.mod())
print("Mod(B)", B.mod())
