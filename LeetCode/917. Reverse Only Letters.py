def reverseOnlyLetters(self, S):
    """
    :type S: str
    :rtype: str
    """
    s = [s for s in S if s.isalpha()]

    if not s:
        return S

    res = []
    for i in range(0, len(S)):
        if not S[i].isalpha():
            res.append(S[i])
        else:
            res.append(s.pop())

    return ''.join(res)
        