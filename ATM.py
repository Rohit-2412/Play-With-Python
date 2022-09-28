# d = deposit
# w = withdraw
# b = balance
# q = quit

def quit():
    print("Thank you for using our ATM, have a nice day!")


class ATM:
    def __init__(self, initialValue):
        self.initialValue = initialValue

    def deposit(self, amount):
        self.initialValue += amount
        print("Successfully deposited", amount)
        print("New balance is", self.initialValue)

    def withdraw(self, amount):
        if amount > self.initialValue:
            print("Insufficient funds")
        else:
            self.initialValue -= amount
            print("Successfully withdrew", amount)
            print("New balance is", self.initialValue)

    def balance(self):
        print(self.initialValue)


print("Welcome to the ATM")
print("d = deposit || w = withdraw || b = balance || q = quit")
choice = input("Would you like to deposit, withdraw, check balance, or quit? ")
user1 = ATM(10000)
while choice != 'q':
    if choice == 'd':
        user1.deposit(int(input("How much would you like to deposit? ")))
    elif choice == 'w':
        user1.withdraw(int(input("How much would you like to withdraw? ")))
    elif choice == 'b':
        user1.balance()
    else:
        print("Invalid input")
    choice = input("Option: ")
quit()