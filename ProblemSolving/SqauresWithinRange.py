def squares(a, b):
    sqrt_a, sqrt_b = a**(1/2), b**(1/2)
    lower = [int(sqrt_a), int(sqrt_a)+1][sqrt_a != int(sqrt_a)]
    upper = int(sqrt_b)

    return upper - lower + 1