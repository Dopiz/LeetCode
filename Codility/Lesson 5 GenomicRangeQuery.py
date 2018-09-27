def solution(S, P, Q):
    # write your code in Python 3.6
    res = []

    for i in range(len(P)):
        target = S[P[i]:Q[i] + 1]
        if 'A' in target:
            res.append(1)
        elif 'C' in target:
            res.append(2)
        elif 'G' in target:
            res.append(3)
        elif 'T' in target:
            res.append(4) 

    return res