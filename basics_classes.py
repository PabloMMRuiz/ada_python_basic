class Fraction:
    def __init__(self, num:int, den:int):
        self.numerator =num
        self.denominator = den
    def __str__(self) -> str:
        return(str(self.numerator) + "/" + str(self.denominator))



if __name__ == "__main__":
    frac1 = Fraction(1,4)
    print(frac1.denominator)
    print(frac1)