# # program for area of circle
import math


radius = eval(input("Enter radius: "))
'''Area of circle'''
# if radius >= 0:
#     area = math.pi * radius * radius
#     print("The area of circle with radius", radius, "is ", area)
# else:
#     print("Radius can't be negative")

'''Circumference of circle'''
if radius >= 0:
    circumference = 2 * math.pi * radius
    print("The circumference of circle with radius", radius, "is", circumference)
else:
    print("Radius can't be negative")

'''for prime number'''
#
# n = int(input("Enter a number to check if its prime or not: "))
# flag = True
# for i in range(2, int(math.sqrt(n))):
#     if n % i == 0:
#         flag = False
#         print("Not a prime number")
#         break
#
# if flag:
#     print("Prime number")
