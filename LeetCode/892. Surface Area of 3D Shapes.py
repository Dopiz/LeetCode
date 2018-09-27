def surfaceArea(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 0:
                res += 2 + grid[i][j] * 4
            if i != 0:
                res -= min(grid[i][j], grid[i - 1][j]) * 2
            if j != 0:
                res -= min(grid[i][j], grid[i][j - 1]) * 2
    return res