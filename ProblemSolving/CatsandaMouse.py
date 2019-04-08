def catAndMouse(x, y, z):
    if abs(x - z) == abs(y - z):
        return "Mouse C"
    if abs(x - z) > abs(y - z):
        return "Cat B"
    return "Cat A"
