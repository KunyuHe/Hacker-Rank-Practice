def minimumDistances(a):
    num_index = dict()
    for i, num in enumerate(a):
        if num not in num_index:
            num_index[num] = [i]
        else:
            if len(num_index[num]) == 1:
                num_index[num].append(i)
            else:
                num_index[num][1] = i

    min_dist = 1000
    for _, pair in num_index.items():
        if len(pair) != 2:
            continue
        dist = pair[1] - pair[0]
        if dist < min_dist:
            min_dist = dist

    if min_dist == 1000:
        return -1
    return min_dist
