def solution(A):
    # write your code in Python 3.6
    if len(A) < 3:
        return 0

    A = sorted(A)

    for i in range(2, len(A)):
        if A[i - 2] + A[i - 1] > A[i]:
            return 1
    
    return 0