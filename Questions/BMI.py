import math

weight = eval(input("Enter weight in kilograms: "))
height = eval(input("Enter height in meters: "))
bmi = weight / math.pow(height, 2)

if bmi < 18.5:
    print("Underweight\n")
elif 18.5 <= bmi <= 24.9:
    print("Normal\n")
elif 25 <= bmi <= 29.9:
    print("Overweight\n")
else:
    print("Obese\n")
