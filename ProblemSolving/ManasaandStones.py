def stones(n, a, b):
    guesses = []

    for i in range(n):
        if a < b:
            small, large = a, b
        else:
            small, large = b, a
        add = (n-1-i)*small + i*large
        if add not in guesses:
            guesses.append(add)

    return guesses
