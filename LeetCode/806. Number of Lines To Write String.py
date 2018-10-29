def numberOfLines(self, widths, S):
    """
    :type widths: List[int]
    :type S: str
    :rtype: List[int]
    """
    length = 0
    line = 1
    for c in S:
        n_length =  widths[ord(c) - ord('a')]
        if length + n_length > 100:
            line = line + 1
            length = n_length
        else:
            length = length + n_length

    return [line, length]