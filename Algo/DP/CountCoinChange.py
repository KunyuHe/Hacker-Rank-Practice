def getWays(n, c):
    if n == 0:
        return 0

    dp_table = [0] * (n + 1)
    dp_table[0] = 1

    for coin in c:
        for i in range(coin, n + 1):
                dp_table[i] += dp_table[i - coin]

    return dp_table[n]
