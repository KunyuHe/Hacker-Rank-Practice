def biggerIsGreater(w):
    # Algorithm: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
    w, ord_w = list(w), [ord(x) for x in w]

    # 1. Find largest index i such that array[i − 1] < array[i]
    suffix_start = len(w) - 1
    while ord_w[max(0, suffix_start - 1)] >= ord_w[suffix_start] and suffix_start != 0:
        suffix_start -= 1
    # If the entire sequence is non-increasing, it is already the last permutation
    if suffix_start == 0:
        return "no answer"

    # 2. Find largest index j such that j ≥ i and array[j] > array[i − 1]
    for i_suffix in range(len(w)-1, suffix_start-1, -1):
        if ord_w[i_suffix] > ord_w[suffix_start-1]:
            # 3. Swap array[j] and array[i − 1]
            preffix_end, suffix_min = w[suffix_start-1], w[i_suffix]
            w[suffix_start-1], w[i_suffix] = suffix_min, preffix_end
            break

    # 4. Reverse the suffix starting at array[i]
    return "".join(w[:suffix_start] + w[suffix_start:][::-1])

