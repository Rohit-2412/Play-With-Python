d = {}
# print(d)
# print(type(d))

record = {"Name": "Ram", "Course": "B.Tech", "Roll number": 25, "Reg Number": 1211}
# print(record)
# print(record["name"])
# print(record["Course"])
# print(record["Roll number"])
# print(record)


print("Key: ", end=' ')
for i in record:
    print(i, end=' ')
    pass

print()
print("Values: ", end=' ')

for i in record.values():
    print(i, end=' ')
    pass

print()
for i, j in record.items():
    print(f'{i} -> {j}')
    pass
