def jumpingOnClouds(c, k):
    current = k % len(c)
    energy = 100 - 1 - [0, 2][int(c[current] == 1)]

    while current:
        current = (current+k) % len(c)
        energy -= 1 + [0, 2][int(c[current] == 1)]
        
    return energy