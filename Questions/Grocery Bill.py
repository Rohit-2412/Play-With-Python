def print_bill():
    n = eval(input("Enter number of grocery items: "))
    grocery_list = []
    for i in range(n):
        name = input(f"Enter item{i + 1} name: ")
        qty = input(f"Enter item{i + 1} quantity: ")
        price = input(f"Enter item{i + 1} price: ")
        grocery_list.append([name, qty, price])
        print()

    print('*' * 27, end='')
    print('BILL', end='')
    print('*' * 28, end='\n\n')

    total_amount = 0
    print('ITEM NAME', end='')
    print('ITEM QUANTITY'.center(40, ' '), end='')
    print('ITEM PRICE'.center(10, ' '))

    for item in grocery_list:
        print('{0:<22}'.format(item[0]), end='')
        print('{0:<27}'.format(item[1]), end='')
        print(item[2])

        total_amount += eval(item[1]) * eval(item[2])

    print('*' * 59, end='\n')
    print(f'TOTAL AMOUNT:: {total_amount}')
    print('*' * 59)


print_bill()
