def serviceLane(width, cases):
    lst = []

    for start, end in cases:
        sub = width[start:end+1]
        lst.append(min(sub))

    return lst
