class Fraction:
    def __init__(self, num:int, den:int):
        if(type(num)!=int or type(den)!=int):
            raise TypeError("Numerator and denominator should be integers")
        if(den<0):
            num, den = num*-1, den*-1
        if(den ==0):
            raise ZeroDivisionError("Denominator can't be 0")
        div = gcd(num, den)
        self.numerator =num//div
        self.denominator = den//div #Integer division: we know the remainder will be 0!

    def __str__(self) -> str:
        if(self.denominator == 1):
            return str(self.numerator)
        return str(self.numerator) + "/" + str(self.denominator) 
    
    def __repr__(self) -> str:
        if(self.denominator == 1):
            return str(self.numerator)
        return str(self.numerator) + "/" + str(self.denominator) 
    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den) 
    #https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types numeric operators
    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other: object):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)
    
    def __truediv__(self, other: object):
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __radd__(self, other): #Implemented (only here) addition with integers or floats, wich is logic. Float addition is crude and uses only truncation
        if(type(other) == int or type(other)==float):
            other = Fraction(int(other), 1)
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __iadd__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)
    #https://docs.python.org/2.7/reference/datamodel.html#object.__lt__ comparation operators
    def __eq__(self, other: object) -> bool:
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator #This makes sure proportional fractions are considered the same. Could be implemented with gcd, but less efficient
        return first_num==second_num
    
    def __lt__(self, other:object)->bool: #Lower than
        return(self.numerator*other.denominator < other.numerator*self.denominator) #Remember that this works beacuse we expect denominators to be greater than 0
    
    def __gt__(self, other:object)->bool: #Greater than
        return(self.numerator*other.denominator > other.numerator*self.denominator)
    
    def __ge__(self, other:object)->bool: #Greater or equal
        return self.numerator*other.denominator >= other.numerator*self.denominator
    def __le__(self, other:object)->bool: #Lower or equal
        return(self.numerator*other.denominator <= other.numerator*self.denominator) #Remember that this works beacuse we expect denominators to be greater than 0

    def get_num(self):
        return self.numerator
    def get_den(self):
        return self.denominator
    


def gcd(m:int,n:int):
    while m%n !=0:
        m,n = n, m%n
    return n

if __name__ == "__main__":
    frac1 = Fraction(1,4)
    frac2 = Fraction(1,2)
    frac3 = Fraction(7,4)
    frac4 =Fraction(-21, 12)
    frac5 =Fraction(21, 1)
    print(frac4.get_num())
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