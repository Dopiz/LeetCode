def solution(X, A):
    # write your code in Python 3.6
    S = set()
    
    for i in range(len(A)):
        S.add(A[i])
        if len(S) == X:
            return i
            
    return -1