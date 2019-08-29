def isValid(s):
    s_dict = {}
    for l in s:
        if l not in s_dict:
            s_dict[l] = 1
        else:
            s_dict[l] += 1

    cnts = s_dict.values()
    if len(set(cnts)) == 1:
        return "YES"
    elif len(set(cnts)) > 2:
        return "NO"
    elif list(cnts).count(max(cnts)) > 1:
        return "NO"
    return "YES"
