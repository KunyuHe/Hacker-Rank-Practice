def isValid(s):
    # Count letters in s
    s_dict = {}
    for l in s:
        if l not in s_dict:
            s_dict[l] = 1
        else:
            s_dict[l] += 1

    # If all letters in s occurs the same time, return "YES"
    cnts = s_dict.values()
    set_cnts = list(set(cnts))
    if len(set_cnts) == 1:
        return "YES"
    # If there are more than 3 unique counts, return "NO"
    elif len(set_cnts) > 2:
        return "NO"

    # With two unique counts, the one occurs only once is either 1 or
    # substracting one from it we can get another
    for i in range(2):
        if list(cnts).count(set_cnts[i]) == 1 and (set_cnts[i] - 1 == set_cnts[i-1] or set_cnts[i] == 1):
            return "YES"
    return "NO"
