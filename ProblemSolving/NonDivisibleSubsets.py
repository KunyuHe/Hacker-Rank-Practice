def nonDivisibleSubset(k, s):
    counts = [0] * k
    # Count thsoe are evenly divisible by k and those are not
    for number in s:
        counts[number % k] += 1

    # Always include one that is evenly divisible by k as adding any others would make
    # the sum not
    count = min(counts[0], 1)
    # Goes until half, and we are comparing i and k-i, including both would not be
    # possible
    for i in range(1, k//2+1):
        if i != k - i:
            count += max(counts[i], counts[k-i])
        else:
            count += min(counter[i], 1)

    return count