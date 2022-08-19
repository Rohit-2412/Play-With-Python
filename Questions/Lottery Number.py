import random

lottery = random.randint(10, 99)
lottery = str(lottery)
guess = input("Enter a 2 digit number: ")

if lottery == guess:
    print("Congratulations!!!")
    print("You guessed it correct")

elif lottery == lottery[::-1]:
    print("Well done!!!")
    print("You guessed correct but in reverse order")

elif lottery[0] == guess[0] or lottery[1] == guess[1] or lottery[0] == guess[1] or lottery[1] == guess[0]:
    print("Good!!!")
    print("You guessed one correct digit")

print(f'Lottery number is {lottery}')
