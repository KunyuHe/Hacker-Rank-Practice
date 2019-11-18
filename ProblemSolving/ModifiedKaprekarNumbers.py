def kaprekarNumbers(p, q):
    lst = []

    for num in range(p, q+1):
        sq = num**2
        sq_str = str(sq)

        cut = len(sq_str) // 2
        try:
            left, right = int(sq_str[:cut]), int(sq_str[cut:])
        except:
            left, right = 0, int(sq_str[cut:])
        if left + right == num:
            lst.append(str(num))

    if not lst:
        print("INVALID RANGE")
        return None
    print(" ".join(lst))
