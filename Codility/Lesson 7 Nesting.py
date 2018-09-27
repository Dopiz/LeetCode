def solution(S):
    # write your code in Python 3.6
    if len(S) % 2:
        return 0

    res = 0
    for s in S:
        if s == '(':
            res += 1
        else:
            res -= 1
        if res < 0:
            return 0
    
    return 1 if not res else 0