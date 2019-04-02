def miniMaxSum(arr):
    sums = [sum(arr[0:i] + arr[i+1:]) for i in range(len(arr))]

    print(min(sums), " ", max(sums))
