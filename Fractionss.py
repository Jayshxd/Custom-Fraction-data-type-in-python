from math import gcd

class Fraction:
    

    def __init__(self,Numerator,Denominator):
        if Denominator==0:
            raise ValueError("Denominator can not be zero")
        common_factor = gcd(Numerator,Denominator)
        self.num=Numerator//common_factor
        self.dem=Denominator//common_factor

    def __str__(self):
        return f"{self.num}/{self.dem}"



    def __add__(self, other):
        temp_num = (self.num * other.dem) + (self.dem * other.num)
        temp_dem = self.dem * other.dem
        common_factor = gcd(temp_num, temp_dem)
        return Fraction(temp_num // common_factor, temp_dem // common_factor)

    def __sub__(self, other):
        temp_num = (self.num * other.dem) - (other.num * self.dem)
        temp_dem = self.dem * other.dem
        common_factor = gcd(temp_num, temp_dem)
        return Fraction(temp_num // common_factor, temp_dem // common_factor)

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_dem = self.dem * other.dem
        common_factor = gcd(temp_num, temp_dem)
        return Fraction(temp_num // common_factor, temp_dem // common_factor)

    def __truediv__(self, other):
        temp_num=self.num*other.dem
        temp_dem=self.dem*other.num
        common_factor = gcd(temp_num,temp_dem)
        if temp_num==temp_dem:
            return Fraction(1,1)
        return Fraction(temp_num//common_factor,temp_dem//common_factor)

    def __floordiv__(self, other):
        return self.num * other.dem // (self.dem * other.num)

    def __gt__(self, other):
        return self.num * other.dem > other.num * self.dem

    def __ge__(self, other):
        return self.num * other.dem >= other.num * self.dem

    def __lt__(self, other):
        return self.num * other.dem < other.num * self.dem

    def __le__(self, other):
        return self.num * other.dem <= other.num * self.dem

    def __eq__(self, other):
        return self.num * other.dem == other.num * self.dem

    def __ne__(self, other):
        return self.num * other.dem != other.num * self.dem

    #Power
    def __pow__(self,power):
        #Anything raise to 0 is 1
        if power==0:
            #We will return new fraction of 1/1 and original will be also safe.
            return Fraction(1,1)
        if power<0:
            #as NEGATIVE power flips num. & denm.
            #So, Here we are just flipping the nums and denms.
            new_num = self.dem ** abs(power)  #abs--> Absolute Value Function : returns the absolute positive.
            new_dem = self.num ** abs(power)
            return Fraction(new_num,new_dem) #--> returing a new Fraction & original is safe.

        return Fraction(self.num**power,self.dem**power) #--> If none of abovw cases are TRUE we will return the new new Fraction & original is safe.

    def get_type(self):
        return "<class 'Fraction'>"









