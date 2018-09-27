def solution(N):
    # write your code in Python 3.6
    N = bin(N)[2:]
    
    if N.count('1') < 2:
        return 0
        
    res = 0
    idx = N.index('1')
    
    while ('1' in N[idx + 1:]):
        next = N[idx + 1:].index('1') + idx + 1
        res = max(res, next - idx - 1)
        idx = next
        
    return res