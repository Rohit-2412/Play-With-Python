# # operator overloading
# class NaturalNumber:
#     def __init__(self, a):
#         self.data = a
#
#     def __add__(self, other):
#         return self.data + other.data
#
#     def __str__(self):
#         return f'data: {self.data}'
#
#     def __sub__(self, other):
#         return self.data - other.data
#
#
# p = NaturalNumber(2)
# q = NaturalNumber(5)
# print(f'{p} + {q} = {p + q}')
# print(f'{p} - {q} = {p - q}')
#
# val1 = 100
# val2 = 50
# print(f'{val1} + {val2} = {val1 + val2}')
# val1 = "Hello, "
# val2 = " Python!"
# print(f'{val1} + {val2} = {val1 + val2}')
# val1 = [1, 2, 3, 4, 5]
# val2 = [10, 11, 12, 13, 14, 15]
# print(f'{val1} + {val2} = {val1 + val2}')

class A:
    def __init__(self, n):
        self.pages1 = n

    def __add__(self, other):
        return self.pages1 + other.pages2

    def __gt__(self, other):
        return self.pages1 > other.pages2


class B:
    def __init__(self, n):
        self.pages2 = n

    def __add__(self, other):
        return self.pages2 + other.pages1

    def __gt__(self, other):
        return self.pages2 > other.pages1


aa = A(10)
bb = B(100)
print(aa + bb)
print(aa > bb)