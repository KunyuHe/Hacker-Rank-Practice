def utopianTree(n):
    height = 1

    for r in range(n):
        if r % 2 == 0:
            height *= 2
        else:
            height += 1

    return height
