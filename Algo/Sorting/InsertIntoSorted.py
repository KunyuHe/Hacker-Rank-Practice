def insertionSort1(n, arr):
    to_insert = arr[-1]

    i = n - 2
    while i >= 0:
        if arr[i] <= to_insert:
            arr[i+1] = to_insert
            break
        else:
            arr[i+1] = arr[i]
        i -= 1
        print(" ".join([str(num) for num in arr]))
    else:
        arr[i+1] = to_insert
    print(" ".join([str(num) for num in arr]))
