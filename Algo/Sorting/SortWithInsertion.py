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
    else:
        arr[i+1] = to_insert

    return arr


def insertionSort2(n, arr):
    if n == 1:
        print(arr[0])

    for i in range(2, n+1):
        arr[:i] = insertionSort1(i, arr[:i])
        print(" ".join([str(num) for num in arr]))
