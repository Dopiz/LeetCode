def binaryGap(self, N):
    """
    :type N: int
    :rtype: int
    """
    n = bin(N)[2:]

    if n.count('1') < 2:
        return 0

    idx = [i for i, val in enumerate(n) if val == '1']
    return max([idx[i] - idx[i - 1] for i in range(1, len(idx))])