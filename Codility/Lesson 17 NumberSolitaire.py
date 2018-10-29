def solution(A):
    # write your code in Python 3.6
    step = [A[0]] * (len(A) + 6)
    
    for i in range(1, len(A)):
        step[i + 6] = max(step[i:i + 6]) + A[i]
    
    return step[-1]