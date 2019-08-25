def circularArrayRotation(a, k, queries):
    # bound k within [0, len(a))
    k = k % len(a)
    rotated = a[(len(a)-k):] + a[:(len(a)-k)]
    return [rotated[i] for i in queries]