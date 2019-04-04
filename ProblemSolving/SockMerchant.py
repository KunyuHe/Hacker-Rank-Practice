def sockMerchant(n, ar):
    return sum([ar.count(col) // 2 for col in set(ar)])
