
# This is a guess the number game. The user has to pick a number between 1 and x. They get 3 tries to guess the number
import random

def guess(x):

    num = random.randint(1,x)
    
    for i in range(4):


        your_num = int(input("Enter a number"))

        if i == 3:
            print("You lost")
            break
        if num == your_num:
            print("Yay! You guessed the number")
            break
        elif num > your_num:
            print("Try a higher number")
        else:
            print("Try a lower number")
    
    print("number was ", str(num))


guess(10)
