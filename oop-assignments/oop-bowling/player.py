from frame import Frame 


class Player(): 
    
    
    def __init__(self, name, allframes=[], score = 0):
        self.name = name
        self.allframes = allframes
        self.score = score
        
    # def calculate_score(self.allframes, score)
    #     for frame in range(0,len(allframes)): 
    #         if Frame.is_strike:
    #             print("Strike")
    #         elif Frame.is_spare: 
    #             print("Spare")
    #         else:
    # #             ("you got less then 10")              

    # def get_frame(Frame):
    #     self 


Bob = Player("Bob")
frame1 = Frame(2,4)
frame2 = Frame(10,0)
frame3 = Frame(5,5)  

Bob.allframes.append(frame1)
Bob.allframes.append(frame2)
Bob.allframes.append(frame3)

for frame in Bob.allframes:
    print(frame)

