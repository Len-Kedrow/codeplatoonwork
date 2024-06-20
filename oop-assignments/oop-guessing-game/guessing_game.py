import random

class GuessingGame():
    def __init__(num):
         self.num = num  

    def guess(userguess, self.num):

        if userguess>self.num:
            return "high"
        elif userguess<self.num: 
            return "low"
        else:
            return f"Your guess of {userguess} is correct. " 

    
   
        








def main():
    print("Let's play a guessing game") 
          
    num = random.randint(1,100)
    game =GuessingGame(num)
    not_solved = 0; 
    while   not_solved == 0:
        userguess = input("Pick number 1-100:  ")
        is_right = game.guess(userguess)
        if is_right == "high" or is_right == "low":
            pass
        else:
            print(is_right)
            not_solved = 1
        "\n"    
    
    