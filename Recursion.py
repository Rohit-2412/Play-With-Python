# normal recursion
def fact1(n):
    if n <= 1:
        return 1
    else:
        return n * fact1(n - 1)

    # tail recursion


def fact2(n, num):
    if n == 1:
        return num
    else:
        return fact2(n - 1, num * n)


print(fact1(6))
print(fact2(5, 1))
