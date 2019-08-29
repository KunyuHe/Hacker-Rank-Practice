def alternatingCharacters(s):
    last = s[0]
    cnt = 0

    for l in s[1:]:
        if l == last:
            cnt += 1
        else:
            last = l

    return cnt
