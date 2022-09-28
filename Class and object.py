# class Table:
#     def __init__(self, w=7, h=5, c="Blue"):
#         self.h = h
#         self.w = w
#         self.c = c
#
#     def display(self):
#         print("Height: ", self.h, end='')
#         print(", Width: ", self.w, end='')
#         print(", Color: ", self.c)
#
#
# t1 = Table()
# t1.display()
#
# t2 = Table(10, 20, "Black")
# t2.display()

# Question

class Student:
    def __init__(self, name, reg, ca1, ca2, ca3):
        self.name = name
        self.reg = reg
        self.ca1 = ca1
        self.ca2 = ca2
        self.ca3 = ca3

    def display(self):
        print(f'Student Name: {self.name} Registration Number: {self.reg}'
              f' Total Marks:{(self.ca1 + self.ca2 + self.ca3) * (100 / 90):.2f}%')
        print()

    def get_sum(self):
        return self.ca1 + self.ca2 + self.ca3


ls = []
for _ in range(3):
    name = input("Enter name: ")
    reg = int(input("Enter Registration Number: "))
    ca1 = int(input("Enter CA1 Marks out of 30 "))
    ca2 = int(input("Enter CA2 Marks out of 30 "))
    ca3 = int(input("Enter CA3 Marks out of 30 "))
    s = Student(name, reg, ca1, ca2, ca3)
    s.display()
    ls.append(s)

highest_marks = 0
for i in ls:
    temp = i.get_sum()
    if temp > highest_marks:
        highest_marks = temp

print("Highest Marks is:", highest_marks)