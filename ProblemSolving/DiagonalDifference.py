def diagonalDifference(arr):
    dim = len(arr)
    for i in range(dim):
        arr[i][i] - arr[i][-1-i]
