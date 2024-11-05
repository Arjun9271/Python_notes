class Fraction:
    def __init__(self,n,d):
        self.num = n
        self.den = d
        
    def __add__(self,other):
        temp_num = self.num*other.den+self.den*other.num
        temp_den = self.den*other.den
        
        return f"{temp_num}/{temp_den}"