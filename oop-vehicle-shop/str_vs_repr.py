class ComplexNumber:
    def __init__(self, real, imag): 
        self.real = real 
        self.imag = imag
    
    def __repr__(self): 
        return f" ComplexNumber( {self.real}, {self.imag})"

    def __str__(self):
        return f"{self.real} + {self.imag}i"
#end class 


c = ComplexNumber(1,-2)
c2 = ComplexNumber(4, 7)
listlist = [c , c2]
print(listlist)
print(c)
# print(repr(c))
# print(str(c))

