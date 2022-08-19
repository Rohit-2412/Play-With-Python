def reverse(n):
    res = ''
    for i in str(n):
        res = i + res
    return int(res)


def is_palindrome(num):
    num = str(num)
    length = len(num) - 1
    for i in range(length):
        if num[i] != num[length - i]:
            return False
    return True


def make_palindrome(num):
    count = 0
    while not is_palindrome(num):
        count += 1
        num += reverse(num)
    print(f'{num} is made palindrome in {count} times')


make_palindrome(9797)
