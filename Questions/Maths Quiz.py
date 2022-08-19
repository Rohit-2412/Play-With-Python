import random

num = int(input("How many questions you want to play? "))

score = 0
operations = ['-', '+', '*']
choice = ''

for i in range(num):
    a = random.randint(1, 15)
    b = random.randint(1, 15)
    choice = random.choice(operations)
    if choice == '-':
        answer = int(input(f'What is {a} {choice} {b}? '))
        if a - b == answer:
            score += 1

    elif choice == '+':
        answer = int(input(f'What is {a} {choice} {b}? '))
        if a + b == answer:
            score += 1

    elif choice == '*':
        answer = int(input(f'What is {a} {choice} {b}? '))
        if a * b == answer:
            score += 1

print(f'You scored {score} out of {num}')
