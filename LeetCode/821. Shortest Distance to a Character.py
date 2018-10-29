def shortestToChar(self, S, C):
    """
    :type S: str
    :type C: str
    :rtype: List[int]
    """
    
    locate = []
    for i in range(0, len(S)):
        if S[i] == C:
            locate.append(i)

    res = []
    for i in range(0, len(S)):
        temp = 10000
        for n in locate:
            if abs(n - i) < temp:
                temp = abs(n - i)
        res.append(temp)

    return res