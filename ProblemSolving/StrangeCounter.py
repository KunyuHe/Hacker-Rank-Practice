def strangeCounter(t):
    # Initial state
    start_t, next_t = 1, 4
    start_v = 3

    while not (t >= start_t and t < next_t):
        start_t = next_t
        start_v *= 2
        next_t = start_t + start_v

    return start_v - (t-start_t)
