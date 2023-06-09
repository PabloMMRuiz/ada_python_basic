class Fraction:
    def __init__(self, num:int, den:int):
        self.numerator =num
        self.denominator = den
    def __str__(self) -> str:
        if(self.denominator == 1):
            return str(self.numerator)
        return str(self.numerator) + "/" + str(self.denominator) 
    
    def __add__(self, frac2):
        brute_num = self.numerator * frac2.denominator + frac2.numerator * self.denominator
        brute_den = self.denominator * frac2.denominator
        gcd_den_num = gcd(brute_num, brute_den)
        return Fraction(brute_num//gcd_den_num, brute_den//gcd_den_num) #Integer division: we know the remainder will be 0!
    #https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types numeric operators
    def __mul__(self, frac2):
        brute_num = self.numerator * frac2.numerator
        brute_den = self.denominator * frac2.denominator
        gcd_den_num = gcd(brute_num, brute_den)
        return Fraction(brute_num//gcd_den_num, brute_den//gcd_den_num)

    def __sub__(self, frac2: object):
        brute_num = self.numerator * frac2.denominator - frac2.numerator * self.denominator
        brute_den = self.denominator * frac2.denominator
        gcd_den_num = gcd(brute_num, brute_den)
        return Fraction(brute_num//gcd_den_num, brute_den//gcd_den_num)
    
    def __truediv__(self, frac2: object):
        brute_num = self.numerator * frac2.denominator
        brute_den = self.denominator * frac2.numerator
        gcd_den_num = gcd(brute_num, brute_den)
        return Fraction(brute_num//gcd_den_num, brute_den//gcd_den_num)


    #https://docs.python.org/2.7/reference/datamodel.html#object.__lt__ comparation operators
    def __eq__(self, frac2: object) -> bool:
        first_num = self.numerator * frac2.denominator
        second_num = frac2.numerator * self.denominator #This makes sure proportional fractions are considered the same. Could be implemented with gcd, but less efficient
        return first_num==second_num
    
    def __lt__(self, frac2:object)->bool:
        return(self.numerator*frac2.denominator < frac2.numerator*self.denominator) #Remember that this works beacuse we expect denominators to be greater than 0
    def __gt__(self, frac2:object)->bool:
        return(self.numerator*frac2.denominator > frac2.numerator*self.denominator)
    


def gcd(m:int,n:int):
    while m%n !=0:
        m,n = n, m%n
    return n

if __name__ == "__main__":
    frac1 = Fraction(1,4)
    frac2 = Fraction(1,2)
    frac3 = Fraction(7,4)
    frac4 =Fraction(21, 12)
    print(frac1.denominator)
    print(frac1)
    print(frac1+frac2)
    print(frac1+frac3)
    print(frac2 == frac3)
    print(frac4 == frac3)
    print(frac1<frac2)
    print(frac1*frac2)
    print(frac1>frac2)
    print(frac3/frac2)
    print(frac2-frac1)
    print(gcd(8,16))
    print(gcd(32,28))