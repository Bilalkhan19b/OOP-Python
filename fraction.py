class Fraction:
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def __add__(self, other):
        temp_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        temp_denominator = self.denominator * other.denominator
        return "{}/{}".format(temp_numerator, temp_denominator)

    def __sub__(self, other):
        temp_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        temp_denominator = self.denominator * other.denominator
        return "{}/{}".format(temp_numerator, temp_denominator)

    def __mul__(self, other):
        temp_numerator = self.numerator * other.numerator
        temp_denominator = self.denominator * other.denominator
        return "{}/{}".format(temp_numerator, temp_denominator)

    def __truediv__(self, other):
        temp_numerator = self.numerator * other.denominator
        temp_denominator = self.denominator * other.numerator
        return "{}/{}".format(temp_numerator, temp_denominator)
