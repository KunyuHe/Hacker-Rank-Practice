def countingSort(arr):
    counter = [0]*100 # as per the constraint that arr[i] < 100

    for num in arr:
        counter[num] += 1

    sorted = []
    for num, cnt in enumerate(counter):
        sorted += [num]*cnt

    return sorted
