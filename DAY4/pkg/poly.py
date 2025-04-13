class Poly:
    def __init__(self, *coefficients):
        self.coefficients = list(coefficients)

    def __add__(self, other):
        len_self = len(self.coefficients)
        len_other = len(other.coefficients)

        if len_self < len_other:
            padded_self = [0] * (len_other - len_self) + self.coefficients
            padded_other = other.coefficients
        else:
            padded_self = self.coefficients
            padded_other = [0] * (len_self - len_other) + other.coefficients

        result = [a + b for a, b in zip(padded_self, padded_other)]
        return Poly(*result)

    def __repr__(self):
        return f"Poly({', '.join(map(str, self.coefficients))})"
