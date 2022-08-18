# type 1 return type = void
def sum(n1, n2):
    z = n1 + n2
    print(z)


sum(10, 20)

'''Types of arguments'''


# default arguments
# positional arguments
# default arguments
# variable length arguments


# type 2 returning value back to a variable
def sum(n1, n2):
    z = n1 + n2
    return z


a = sum(25, 15)
print(a)


# type 3 printing the value returned by the function
def sum(n1, n2):
    z = n1 + n2
    return z


print(sum(5, 5))
