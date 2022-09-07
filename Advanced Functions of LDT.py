x = [10, 20, 30]
y = [10, 25, 35, 45]

res = []
for i in x:
    for j in y:
        if i != j:
            res.append([i, j])

print(res)

# List comprehension
# variable = [ expression | for var in seq | for var in seq | condition check]
lc = [[i, j] for i in x for j in y if i != j]
print(lc)
