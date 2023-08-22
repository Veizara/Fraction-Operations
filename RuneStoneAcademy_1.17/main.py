
def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class Fraction:
    def __init__(self,numerator, determinator):
        self.num = numerator
        self.det = determinator

    def getNum(self):
        return self.num

    def getDet(self):
        return self.det

    def __add__(self, otherFraction):
        new_numerator = self.num * otherFraction.det + otherFraction.num * self.det
        new_determinator = otherFraction.det * self.det
        common = GCD(new_numerator,new_determinator)
        return Fraction(new_numerator// common , new_determinator//common)

    def __sub__(self, otherFraction):
        new_numerator = self.num * otherFraction.det - otherFraction.num * self.det
        new_determinator = otherFraction.det * self.det
        common = GCD(new_numerator,new_determinator)
        return Fraction(new_numerator//common , new_determinator // common)

    def __mul__(self, otherFraction):
        new_numerator = self.num * otherFraction.num
        new_determinator = otherFraction.det * self.det
        common = GCD(new_numerator,new_determinator)
        return Fraction(new_numerator//common , new_determinator//common)

    def __truediv__(self, otherFraction):
        new_numerator = self.num * otherFraction.det
        new_determinator = self.det * otherFraction.num
        common = GCD(new_numerator,new_determinator)
        return Fraction(new_numerator//common , new_determinator//common)

    def __gt__(self, otherFraction):
        if(self.det == otherFraction.det):
            return self.num > otherFraction.num
        else:
            first_numerator = self.num * otherFraction.det
            second_numerator = self.det * otherFraction.num
            return first_numerator > second_numerator

    def __ge__(self, otherFraction):
        if (self.det == otherFraction.det):
            return self.num >= otherFraction.num
        else:
            first_numerator = self.num * otherFraction.det
            second_numerator = self.det * otherFraction.num
            return first_numerator >= second_numerator
    def __lt__(self, otherFraction):
        if(self.det == otherFraction.det):
            return self.num < otherFraction.num
        else:
            first_numerator = self.num * otherFraction.det
            second_numerator = self.det * otherFraction.num
            return first_numerator < second_numerator

    def __le__(self, otherFraction):
        if (self.det == otherFraction.det):
            return self.num <= otherFraction.num
        else:
            first_numerator = self.num * otherFraction.det
            second_numerator = self.det * otherFraction.num
            return first_numerator <= second_numerator
    def __ne__(self, otherFraction):
        if (self.det == otherFraction.det):
            return self.num != otherFraction.num
        else:
            first_numerator = self.num * otherFraction.det
            second_numerator = self.det * otherFraction.num
            return first_numerator != second_numerator

    def __radd__(self, otherFraction):
        otherFraction = Fraction(otherFraction,1)
        new_numerator = self.num * otherFraction.det + otherFraction.num * self.det
        new_determinator = otherFraction.det * self.det
        common = GCD(new_numerator, new_determinator)
        return Fraction(new_numerator // common, new_determinator // common)

    def __iadd__(self, otherFraction):
        new_numerator = self.num * otherFraction.det + otherFraction.num * self.det
        new_determinator = otherFraction.det * self.det
        common = GCD(new_numerator, new_determinator)
        self.num = new_numerator // common
        self.det = new_determinator // common
        return self


fraction1 = Fraction(2,3)
fraction2 = Fraction(2,3)

sum_fraction = fraction1 + fraction2
sub_fraction = fraction1 - fraction2
mult_fraction = fraction1 * fraction2
div_fraction = fraction1 / fraction2
gt_check = fraction1 > fraction2
ge_check = fraction1 >= fraction2
lt_check = fraction1 < fraction2
le_check = fraction1 <= fraction2
ne_check = fraction1 != fraction2
fraction1 += fraction2
print("First fraction numerator: %d  and Second fraction numerator: %d "
      "\nFirst fraction determinator: %d and Second Fraction determinator: %d "
      %(fraction1.getNum(),fraction2.getNum(),fraction1.getDet(),fraction2.getDet()))
print("Result of addition %d/%d " %(sum_fraction.getNum(),sum_fraction.getDet()))
print("Result of substraction %d/%d " %(sub_fraction.getNum(),sub_fraction.getDet()))
print("Result of multiplication %d/%d " %(mult_fraction.getNum(),mult_fraction.getDet()))
print("Result of division %d/%d " %(div_fraction.getNum(),div_fraction.getDet()))
print(fraction1.getNum(), "/", fraction1.getDet())
print(gt_check) # >
print(ge_check) # >=
print(lt_check) # <
print(le_check) # <=
print(ne_check) # !=


