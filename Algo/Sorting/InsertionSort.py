def insertionSort(l):
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
    return l


def runningTime(arr):
    cnt = 0

    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
            cnt += 1
        arr[j+1] = key

    return cnt
