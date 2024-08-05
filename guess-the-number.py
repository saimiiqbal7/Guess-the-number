
# This is a guess the number game. The user has to pick a number between 1 and x. They get 3 tries to guess the number
import random

def guess(x):
    num = random.randint(1, x)
    attempts = 3
    print(f"Guess the number between 1 and {x}. You have {attempts} tries.")

    for i in range(attempts):
        your_num = int(input("Enter a number: "))

        if num == your_num:
            print("Yay! You guessed the number!")
            break
        elif num > your_num:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
        
        if i == attempts - 1:
            print("You lost. The number was", num)

guess(10)

