def fairCandySwap(self, A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    diff = (sum(A) - sum(B)) // 2
    A, B = set(A), set(B)
    for a in A:
        if a - diff in B:
            return [a, a - diff]