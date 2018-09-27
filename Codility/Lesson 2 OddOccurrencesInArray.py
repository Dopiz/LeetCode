def solution(A):
    # write your code in Python 3.6
    res = 0
    for num in A:
        res ^= num
        
    return res