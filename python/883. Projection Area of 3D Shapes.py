def projectionArea(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    x = sum(v > 0 for row in grid for v in row)
    y = sum(map(max, grid))
    z = sum(map(max, zip(*grid)))

    return x + y + z