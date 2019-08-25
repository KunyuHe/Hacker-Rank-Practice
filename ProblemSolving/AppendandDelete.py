def appendAndDelete(s, t, k):
    n_s, n_t = len(s), len(t)
    
    # If short enough, no need to further
    if n_s + n_t <= k:
        return "Yes"
    
    # Count until the first different char, use zip so that ends with the shorter one
    same = 0
    for l_s, l_t in zip(s, t):
        if l_s == l_t:
            same += 1
        else:
            break
    n_diff = (n_s - same) + (n_t - same)
    
    # If doable
    if n_diff <= k and n_diff % 2 == k % 2:
        return "Yes"
    return "No"