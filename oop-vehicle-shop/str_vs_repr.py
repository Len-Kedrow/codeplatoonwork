


# class ComplexNumber:
#     def __init__(self, real, imag): 
#         self.real = real 
#         self.imag = imag
    
#     def __repr__(self): 
#         return f" Complex Number( {self.real}, {self.imag})"

#     def __str__(self):
#         return f"{self.real} + {self.imag}i"
# #end class 


# c = ComplexNumber(1,-2)
# print(repr(c))

# print(str(c))

class MyClass:
    instances =[]

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

        MyClass.instances.append(self)

    def __str__ (self):
        return f"{self.val1} + {self.val2} "
    
    @classmethod
    def print_all_instnaces(cls):
        current_cars=[]
        for instance in cls.instances: 
            print(instance)
       
#end class

obj1 = MyClass("val1-1", "val2-1")
obj2 = MyClass("val1-2", "val2-2")
obj3 = MyClass("val1-3", "val2-3")

MyClass.print_all_instnaces()

