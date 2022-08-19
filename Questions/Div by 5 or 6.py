print("Printing numbers from 100 to 1000 which are either divisible by 5 or 6")
for i in range(100, 1001):
    if i % 5 == 0 and i % 6 != 0:
        print(i, end=' ')

    elif i % 6 == 0 and i % 5 != 0:
        print(i, end=' ')
