#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countSwaps function below.
def countSwaps(a, n):
    cnt = 0
    arr = a[:]

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                cnt += 1
    print(("Array is sorted in %s swaps.\n"
           "First Element: %s\n"
           "Last Element: %s" % (cnt, arr[0], arr[-1])))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a, n)
