import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
totalSum = dice1 + dice2
point = 0
if totalSum == 7 or totalSum == 11:
    status = 'win'
elif totalSum == 2 or totalSum == 3 or totalSum == 12:
    status = 'lose'
else:
    status = 'continue'
    point = totalSum

while status == 'continue':
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    totalSum = dice1 + dice2
    if totalSum == 7:
        status = 'lose'
    if totalSum == point:
        status = 'win'

print('Player', status)
