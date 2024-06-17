class Frame():
    is_strike = False
    is_spare = False
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2

        if b1 == 10: 
            self.is_strike = True
        elif b1+b2==10: 
            self.is_spare = True
        else: 
            pass
        #def __str__(self):



# frame1 = Frame(2,4)
# frame2 = Frame(10,0)
# frame3 = Frame(5,5)        
        

# if frame3.is_strike:
#     print("Strike")
# elif frame3.is_spare: 
#     print("Spare")
# else:
#     ("you got less then 10")