def numSpecialEquivGroups(self, A):
    """
    :type A: List[str]
    :rtype: int
    """
    list = []
    for s in A:
        list.append(sorted(s[0::2]) + sorted(s[1::2]))
        
        
    res = []
    for s in list:
        word = ''
        for c in s:
            word = word + c
        res.append(word)
        
    return len(set(res))