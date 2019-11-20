def happyLadybugs(b):
    cnts = dict()
    for i in range(n):
        # Count each type of cell
        if b[i] not in cnts:
            cnts[b[i]] = 1
        else:
            cnts[b[i]] += 1

    # If only one, cannot be happy
    for cell in set(b):
        if cell != "_" and cnts[cell] == 1:
            return "NO"
    
    if cnts.get("_", 0) == 0:
        for i in range(1, n-1):
            if b[i-1] != b[i] and b[i+1] != b[i]:
                return "NO"
    return "YES"
