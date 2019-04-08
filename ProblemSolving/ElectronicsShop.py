def getMoneySpent(keyboards, drives, b):
    max_total, min_total = 0, 10000000

    for keyboard in keyboards:
        for drive in drives:
            total = keyboard + drive
            if total > max_total and total <= b:
                max_total = total
            if total < min_total:
                min_total = total

    if min_total > b:
        return -1
    return max_total
