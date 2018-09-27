def solution(A):
    # write your code in Python 3.6
    right = sorted([k + v for k, v in enumerate(A)])
    left  = sorted([k - v for k, v in enumerate(A)])

    j = 0
    count = 0
    
    for i, v in enumerate(right):
        while j < len(right) and v >= left[j]:
            count += j - i
            j = j + 1
        if count > 1e7:
            return -1
    
    return count