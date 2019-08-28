def arrayManipulation(n, queries):
    # Since the right and left index start at 1
    lst = [0] * (n+1)

    # Since each query would add k to elements between (a-1) and (b-1)
    for i in range(len(queries)):
        a, b, k = queries[i]
        lst[a - 1] += k
        lst[b] -= k

    # Add elements from left to right, each k would span (a-1) to (b-1)
    sum_max, num_sum = 0, 0
    for num in lst:
        num_sum += num
        if num_sum > sum_max:
            sum_max = num_sum
    return sum_max
