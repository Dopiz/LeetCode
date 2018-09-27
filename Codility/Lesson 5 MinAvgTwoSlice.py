def solution(A):
    # write your code in Python 3.6
    min_avg = 10001
    idx = 0

    for i in range(0, len(A) - 1):
        if (A[i] + A[i+1]) / 2 < min_avg:
            min_avg = min((A[i] + A[i+1]) / 2, min_avg)
            idx = i
        if i < len(A) - 2 and (A[i] + A[i+1] + A[i+2]) / 3 < min_avg:
            min_avg = min((A[i] + A[i+1] + A[i+2]) / 3, min_avg)
            idx = i
    
    return idx