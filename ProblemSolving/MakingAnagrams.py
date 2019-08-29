def makeAnagram(a, b):
    shared = {}
    for l in a:
        if l not in shared:
            shared[l] = 1
        else:
            shared[l] += 1

    not_in_a = 0
    for l in b:
        if l not in shared:
            not_in_a += 1
        else:
            shared[l] = shared[l] - 1

    diff = not_in_a
    for cnt in shared.values():
        diff += abs(cnt)

    return diff
