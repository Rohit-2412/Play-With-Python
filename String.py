""" length of string """

# s = "Core python"
# z = len(s)
# print(z)

# message = "hello"
# i = 0
#
# while i < len(message):
#     print("message", "[", i, "] = ", message[i])
#     i += 1
#
# print('-' * 60)
#
# index = 0
# for i in message:
#     print("message", "[", index, "] =", i)

# s = "The food is very tasty"
# ls = ['a', 'e', 'i', 'o', 'u']
#
# for i in s:
#     if i not in ls:
#         print(i, end='')
#
# print()
# print(' ' * 100)
#
# s1 = ""
# s2 = "hello"
# s3 = "world"
# s = s1 + s2
# s4 = s + s3
# print(s)
# print(s4)

''' Pattern
A
A B
A B C
A B C D
A B C D E
'''
# ascii of A = 65
# ascii of a = 97

# n = int(input("> "))
#
# for i in range(n + 1):
#     a = 65
#     for j in range(i):
#         print(chr(a), end='')
#         a += 1
#     print()

# count occurrences of a character
# sentence = "core python"
# key = 'e'
# idx = 0
# for i in sentence:
#     if key == i:
#         print(idx)
#     idx += 1

# print(sentence[0:9:1])
# print(sentence[0:9:2])
# print(sentence[::])
# print(sentence[2:4:1])
# print(sentence[::2])
# print(sentence[2::])
# print(sentence[:4:])
# print(sentence[-4:-1])
# print(sentence[-4:-1])
# print(sentence[-6::])
# print(sentence[-1::-1])


p = []
players = ['a', 'b', 'c', 'd', 'e']
print(players)
# players[0] = "abc"
# players.insert(2, 'something')
players.append('new element')
print(players)

# print(type(p))
# print(type(players))
