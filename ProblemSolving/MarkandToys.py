def maximumToys(prices, k):
    prices.sort()
    cnt = 0

    for price in prices:
        k -= price
        if k < 0:
            break
        cnt += 1

    return cnt
