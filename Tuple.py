t1 = (1, 2, 3, 4)
print(t1)
t2 = (5, 6, 7, 8)
t3 = (9, 10, 11)
# print(t1 + t2 + t3)
del t3
# print(t1 + t2)
# print(type(t))
for i in t1:
    print(i)

''' Operation tuples not support '''
# remove
# pop
# append
# sort
# reverse
# insert

# append in tuples
te = ()
to = ()
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in t:
    if not i % 2:
        te = te + (i,)
    else:
        to = to + (i,)

print(t)
print(to)
print(te)
