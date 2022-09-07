# # insert function
# ls = []
# ls.insert(0, 5)
# print(ls)
# ls.insert(1, 10)
# print(ls)
# ls.insert(0, 6)
# print(ls)
#
# # pop function
# # ls.pop({index})
# ls.pop()
# print(ls)
#
# # remove function
# # ls.remove({element})
# ls.remove(5)
# print(ls)

# Aliasing
"""
If changes are made in copy of original llist then the change will also reflect in original
"""
a = [1, 2, 3]
b = a
b[0] = 100
# print(a)
# print(b)

# Cloning
""" 
If changes are made in copy of original llist then the change will not also reflect in original
"""
c = [1, 2, 3, 4]
d = c[:]
d[2] = 100
# print(c)
# print(d)

# 2d list
arr = [[[i for i in range(4)] for j in range(4)] for k in range(4)]

for i in arr:
    for j in i:
        print(j)
