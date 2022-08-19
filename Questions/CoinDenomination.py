def coins_count(n):
    denominations = [1, 2, 5, 10, 50, 100]
    denominations.sort(reverse=True)
    count = 0
    coins = {}
    for i in denominations:
        if n // i > 0:
            coins.__setitem__(i, n // i)
            count += n // i
            n = n % i
    print(coins)
    print(count)


coins_count(512)
