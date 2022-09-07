# players = {}
# 5 player
# key = name, value = list of 5 scores
# name with total score
# man of series with the highest score
import random

players = {"Virat": [random.randint(10, 99)],
           "Rohit": [100, 10, 10, 100, 10],
           "Rahul": [10, 10, 10, 100, 10],
           "Bhuvi": [10, 10, 10, 100, 10],
           "Maxwell": [10, 10, 10, 100, 10]}

maxScore = 0
name = ""
for i, j in players.items():
    totalScore = sum(j)
    if totalScore > maxScore:
        maxScore = totalScore
        name = i
print(f'Man of the series is {name} with a score of {maxScore}')
print(players)
