def count(s, t, loc, lst):
    return sum([(loc + dist) >= s and (loc + dist) <= t for dist in lst])


def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(count(s, t, a, apples))
    print(count(s, t, b, oranges))
