def getTotalX(a, b):
    count = 0

    for num in range(max(a), min(b) + 1):
        if all([num % elem == 0 for elem in a]) and \
           all([elem % num == 0 for elem in b]):
            count += 1

    return count
