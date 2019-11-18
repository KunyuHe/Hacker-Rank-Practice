def beautifulTriplets(d, arr):
    if len(arr) < 3:
        return 0

    num_cnt = dict()
    num_unique = set(arr)
    trip_cnt = 0

    for num in num_unique:
        num_cnt[num] = arr.count(num)

    for num in num_unique:
        if num + 2*d > arr[-1]:
            break

        if num + d not in num_cnt or num + 2*d not in num_cnt:
            continue
        else:
            trip_cnt += num_cnt[num]*num_cnt[num+d]*num_cnt[num+2*d]

    return trip_cnt
