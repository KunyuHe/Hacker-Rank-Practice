def quickSort(arr):
    pivot = arr[0]
    left, right, equal = [], [], [pivot]

    for num in arr[1:]:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)

    return left + equal + right
