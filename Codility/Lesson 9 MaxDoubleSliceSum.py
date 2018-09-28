def solution(A):
    # write your code in Python 3.6
    max_left = max_ending = max_slice = 0
    
    for i in range(3, len(A)):
        max_left   = max(max_left + A[i - 2], A[i - 2])
        max_ending = max(max_left, A[i - 1], max_ending + A[i - 1])
        max_slice  = max(max_ending, max_slice)
        
    return max_slice