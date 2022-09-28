t = int(input())
for k in range(t):
    l = input().split()
    cats = int(l[0])
    dogs = int(l[1])
    legs = int(l[2])
    max_legs = (cats + dogs) * 4
    min_legs = dogs * 4
    remaining_cats = cats - (2 * dogs)
    if remaining_cats > 0:
        min_legs += remaining_cats * 4
    if legs < min_legs or legs > max_legs or legs % 4 != 0:
        print('no')
    else:
        print('yes')
