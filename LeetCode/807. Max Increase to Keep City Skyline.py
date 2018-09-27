def maxIncreaseKeepingSkyline(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    col = [max(n) for n in grid]
    row = [max(n) for n in zip(*grid)]
    diff = 0

    for i in range(len(col)):
        diff += sum([min(col[i], j) for j in row]) - sum(grid[i])

    return diff