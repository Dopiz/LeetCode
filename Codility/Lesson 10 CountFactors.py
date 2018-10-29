def solution(N):
    # write your code in Python 3.6
    if N == 1:
        return 1
        
    res = 0
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            res = res + 2
    
    if i * i == N:
        res = res - 1
        
    return res