def encryption(s):
    s = s.replace(" ", "")
    l = len(s)
    nrow, ncol = int(l**0.5), [int(l**0.5)+1, int(l**0.5)][int(l**0.5)==l**0.5]
    if nrow*ncol < l:
        nrow = ncol

    output = ["" for _ in range(ncol)]
    for i in range(l):
        output[i % ncol] += s[i]

    return " ".join(output)
