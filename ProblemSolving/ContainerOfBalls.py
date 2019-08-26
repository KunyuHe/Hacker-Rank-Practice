def organizingContainers(container):
    n = len(container)

    # For any given container, if we want to make it contain only one
    # type `a`, then count of non `a` of it must equals sum of counts
    # of all `a` in all other containers. Add count of `a` in the
    # container to both ends, count of all balls in the container
    # equals count of all `a` balls, row = col
    rows, cols = [], [0]*n
    for i in range(n):
        rows.append(sum(container[i]))
        for j in range(n):
            cols[j] += container[i][j]
    if sorted(rows) == sorted(cols):
        return "Possible"
    return "Impossible"
