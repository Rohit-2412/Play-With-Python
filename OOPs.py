# class Person:
#     def __init__(self, name="", age="18"):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(f'Name: {self.name} Age: {self.age}')
#
#
# class Student(Person):
#     def __init__(self, name, age, roll, reg_num):
#         super().__init__(name, age)
#         # Person.__init__(self, name, age)
#         self.roll = roll
#         self.reg_num = reg_num
#
#     def display(self):
#         # Person.display(self)
#         super().display()
#         print(f'Roll Number: {self.roll} Reg. No.: {self.reg_num}')
#
#
# class Teacher(Person):
#     def __init__(self, name, age, salary, dept):
#         Person.__init__(self, name, age)
#         # super().__init__()
#         self.salary = salary
#         self.dept = dept
#
#     def __str__(self):
#         super.__str__(self)
#         return f'Salary: {self.salary} Reg. No.: {self.dept}'
#
#
# # p1 = Person("Rohan", 18)
#
# s1 = Student("Ram", 15, 4, 121132)
# s1.display()
#
# t1 = Teacher("Arun", 45, 10000, "CSE")

class Polygon:
    def __init__(self, perimeter):
        self.x = perimeter

    def __str__(self):
        return f'x: {self.x}'


class Square(Polygon):
    def __init__(self, perimeter, side):
        Polygon.__init__(self, perimeter)
        self.side = side

    def __str__(self):
        return super().__str__() + f' y: {self.side}'


class Rectangle(Square):
    def __init__(self, perimeter, side, width):
        Square.__init__(self, perimeter, side)
        self.width = width

    def __str__(self):
        return super().__str__() + f' width: {self.width}'


obj1 = Polygon(1)
print(obj1)
obj2 = Square(1, 2)
print(obj2)
obj3 = Rectangle(1, 2, 3)
print(obj3)