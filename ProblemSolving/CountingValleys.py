def countingValleys(n, s):
    height, heights, valley, valley_count = 0, [0], None, 0

    for step in s:
        height += {"U": 1, "D": -1}[step]
        heights.append(height)
    
    for i in range(len(heights)):
        if heights[i] == 0 and valley == "Enter":
            valley = None
            valley_count += 1
        if i != len(heights) - 1 and heights[i] == 0 and heights[i + 1] < 0:
            valley = "Enter"
            
    return valley_count
