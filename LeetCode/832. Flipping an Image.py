def flipAndInvertImage(self, A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    for l in A:
        l.reverse()
        for index, num in enumerate(l):
            l[index] = num ^ 1
            
    return A