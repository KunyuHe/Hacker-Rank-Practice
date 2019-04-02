def diagonalDifference(arr):
    sum = 0

    for i in range(len(arr)):
        sum += arr[i][i] - arr[i][-1-i]
    
    return abs(sum)
