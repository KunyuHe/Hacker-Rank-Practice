from bisect import insort, bisect_left


# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    n = len(expenditure)
    if n <= d:
        return 0

    trailing = sorted(expenditure[:d])
    cnt = 0
    mid = int(d / 2)
    for i, add in enumerate(expenditure[d:]):
        if d % 2 == 0:
            threshold = trailing[mid] + trailing[mid - 1]
        else:
            threshold = 2*trailing[mid]
        if add >= threshold:
            cnt += 1

        rem = expenditure[i]
        del trailing[bisect_left(trailing, rem)]
        insort(trailing, add)
    
    return cnt
