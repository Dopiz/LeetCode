def largestTriangleArea(self, points):
    """
    :type points: List[List[int]]
    :rtype: float
    """
    max_area = 0
    p_list = list(itertools.combinations(points, 3))
    
    for p in p_list:
        max_area = max(0.5 * 
                        abs(p[0][0] * p[1][1] + p[1][0] * p[2][1] + p[2][0] * p[0][1] 
                            - p[0][1] * p[1][0] - p[1][1] * p[2][0] - p[2][1] * p[0][0]), max_area)

    return max_area