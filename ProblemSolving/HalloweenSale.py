def howManyGames(p, d, m, s):
    if p > s:
        return 0
    elif p == s:
        return 1

    cnt, s = 1, s - p
    while p - d > m:
        p -= d
        s -= p
        if s < 0:
            break
        cnt += 1
    else:
        cnt += s // m

    return cnt
