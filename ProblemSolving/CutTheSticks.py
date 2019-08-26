def cutTheSticks(arr):
    counts = [len(arr)]

    while len(set(arr)) > 1:
        shortest = min(arr)
        arr = [stick - shortest for stick in arr if stick - shortest != 0]
        counts.append(len(arr))

    return counts