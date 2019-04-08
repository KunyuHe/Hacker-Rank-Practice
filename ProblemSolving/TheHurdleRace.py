def hurdleRace(k, height):
    diff = max(height) - k

    if diff <= 0:
        return 0
    return diff
