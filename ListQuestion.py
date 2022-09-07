n = int(input())
ls = []
for _ in range(n):
    z = input().split()
    if z[0] == 'insert':
        ls.insert(int(z[1]), int(z[2]))
    elif z[0] == 'append':
        ls.append(int(z[1]))
    elif z[0] == 'remove':
        ls.remove(int(z[1]))
    elif z[0] == 'pop':
        ls.pop()
    elif z[0] == 'print':
        print(ls)
    elif z[0] == 'reverse':
        ls.reverse()
    elif z[0] == 'sort':
        ls.sort()
