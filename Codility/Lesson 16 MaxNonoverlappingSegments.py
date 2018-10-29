def solution(A, B):
    # write your code in Python 3.6
    if not A or not B:
        return 0
        
    end = B[0]
    count = 1
    
    for i in range(1, len(A)):
        if A[i] > end:
            count = count + 1
            end = B[i]
    
    return count