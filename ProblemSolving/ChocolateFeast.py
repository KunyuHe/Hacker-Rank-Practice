def chocolateFeast(n, c, m):
    cnt = n // c
    if cnt < 2:
        return cnt

    wrappers = cnt
    while wrappers >= m:
        chocolates = wrappers // m
        cnt += chocolates
        wrappers = chocolates + wrappers % m

    return cnt
