def printArea(width=1, height=2):
    area = width * height
    print(area)


printArea()  # default arguments
printArea(4, 2.5)  # positional arguments
printArea(height=5, width=3)  # keyword arguments
printArea(width=1.5)
printArea(height=1.5)


# Question::
def fun(a, b):
    pass


# fun(a=2, 5)  # SyntaxError: positional argument follows keyword argument
# fun(5, b=3)  # No error
# fun(5, a=3)  # Error - TypeError: fun() got multiple values for argument 'a'

""" Variable length arguments """


# * is known as wild card character
def func(name, *fav_subjects):
    print(name, "likes: ")
    # iterating over fav_subjects
    for subject in fav_subjects:
        print(subject)
    print('-' * 50)


func("Rahul", "C", "C++", "Java", "Python", "JavaScript", "Php", "Kotlin", "TypeScript", "Visual Basic", "R")
func("Vikas", "C")
func("Ram", "Python", "Java", "JavaScript")

''' Returning multiple values from a function'''


def sort(n1, n2):
    if n1 < n2:
        return n1, n2
    else:
        return n2, n1


a, b = sort(50, 5)
print(f'a = {a}, b= {b}')

''' Local and global variable'''


def func3(a, b):
    c = a + b  # local variable `c`
    global d  # declaring a global variable
    d = a + b


func3(10, 5)
# print(c)  # error : due to access level of c. It is a local variable of function
# print(d)  # d = 15 because it's a global variable now

'''Lambda function also known as Anonymous function'''
# Syntax = Name = lambda(variables): Code
# lamda function to find the cube of a number
cube = lambda x: x * x * x
print(f'Cube of 5 is {cube(5)}')
