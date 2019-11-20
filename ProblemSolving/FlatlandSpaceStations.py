def flatlandSpaceStations(n, c):
    c = sorted(c)
    max_dist = max(c[0], n - c[-1] - 1)
    for i in range(1, len(c)):
        dist = c[i] - c[i-1]
        max_dist = max(dist//2, max_dist)
    return max_dist
