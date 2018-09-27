def solution(A):
    # write your code in Python 3.6
    A = set(A)
    
    for num in range(1, len(A) + 1):
        if not num in A:
            return num
    return num + 1