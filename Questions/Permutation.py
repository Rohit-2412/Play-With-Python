def permute_unique(arr):
    permutation = []
    result = []
    count = {n: 0 for n in arr}
    for n in arr:
        count[n] += 1

    def dfs():
        if len(permutation) == len(arr):
            result.append(permutation.copy())
            return

        for num in count:
            if count[num] > 0:
                permutation.append(num)
                count[num] -= 1

                dfs()

                # Backtracking
                permutation.pop()
                count[num] += 1

    dfs()
    return result


# for item in permute_unique([1, 8, 4, 8]):
#     for ls in item:
#         print(ls, end='')
#     print()

if __name__ == '__main__':
    x = 1
    y = 2
    z = 4

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            for k in range(1, z + 1):
                if i != j or j != k:
                    print(i, j, k)
