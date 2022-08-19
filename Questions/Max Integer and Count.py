print("Enter one number in each line. 0 for exiting from the loop")

n = int(input("> "))
max_number = float('-inf')
count = 0
while n != 0:
    if max_number < n:
        max_number = n
        count = 1
    elif n == max_number:
        count += 1
    n = int(input("> "))

print(f'Maximum number is {max_number} with {count} occurrences')
