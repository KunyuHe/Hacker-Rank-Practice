def countingValleys(n, s):
    height, heights = 0, [0]

    for step in s:
        height += {"U": 1, "D": -1}[step]
        heights.append(height)