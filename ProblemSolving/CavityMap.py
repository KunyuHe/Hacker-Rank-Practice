def cavityMap(grid):
    m, n = len(grid[0]), len(grid)
    if n < 3 or m < 3:
        return grid

    for i in range(1, m-1):
        for j in range(1, n-1):
            adjacent = [grid[i-1][j], grid[i+1][j],
                        grid[i][j+1], grid[i][j-1]]
            if "X" in adjacent:
                continue
            if int(grid[i][j]) > max(map(int, adjacent)):
                grid[i] = grid[i][:j] + "X" + grid[i][j+1:]

    return grid
