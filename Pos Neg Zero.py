num = int(input("Enter a number: "))
positive_number = 0

while num != -1:
    if num > 0:
        print("Positive")
        positive_number += 1
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
    num = int(input("Enter a number: "))

print("Total positive number: ", positive_number)
