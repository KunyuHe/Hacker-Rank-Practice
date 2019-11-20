def fairRations(B):
    """
    Chain of even and odds. Like OEEEO, to make it all E, need to swap the two
    Os together, costing number of Es in between. Same from left all right.
    """
    searching = False
    loaves = 0
    swaps = 0

    for n in B:
        if n % 2 == 1:
            if searching:
                loaves += 2 * (swaps+1)
                searching = False
                swaps = 0
            else:
                searching = True
        else:
            if searching:
                swaps += 1

    if searching:
        return "NO"
    return loaves
