def uncommonFromSentences(self, A, B):
    """
    :type A: str
    :type B: str
    :rtype: List[str]
    """
    words = list(A.split(' ')) + list(B.split(' '))
    return [word for word in words if words.count(word) < 2]