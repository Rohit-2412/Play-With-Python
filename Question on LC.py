t = int(input())
for k in range(t):
    n = int(input())
    res = 0
    a = 10
    for i in range(a ** (n - 1), a ** n):
        if i % 2 != 0 and i % 3 == 0 and i % 9 != 0:
            res = i
            break
    print(f'n = {n} answer = {res}')
