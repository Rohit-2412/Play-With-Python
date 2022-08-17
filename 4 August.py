# program 6
acc_number = int(input("Enter account number: "))
customer_type = input("Enter code R/r or B/b: ")

if customer_type.lower() == 'r':
    num_of_channels = int(input("Enter number of premium channels: "))
    bill = 4.5 + 20.50 + num_of_channels * 7.50
    print(f"Generated bill for Residential customer with account number {acc_number} is: {bill}")

elif customer_type.lower() == 'b':
    num_of_connections = int(input("Enter number of service connections: "))
    num_of_channels = int(input("Enter number of premium channels: "))
    bill = 0
    if num_of_connections >= 10:
        bill += 10 * 75
        bill += (num_of_connections - 10) * 5
    else:
        bill += num_of_connections * 75

    bill += num_of_channels * 50
    print(f"Generated bill for Business customer with account number {acc_number} is: {bill}")

else:
    print("Wrong input!")
