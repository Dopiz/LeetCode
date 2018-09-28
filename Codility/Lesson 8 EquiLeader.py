import collections

def solution(A):
    # write your code in Python 3.6
    val = collections.Counter(A).most_common(1)[0][0]
    cnt = collections.Counter(A).most_common(1)[0][1]
    
    if cnt <= len(A) / 2:
        return 0
    
    left, right, count = 0, cnt, 0
    
    for i in range(len(A)):
        if A[i] == val:
            left = left + 1
            right = right - 1
        
        if left > (i + 1) / 2 and right > (len(A) - (i + 1)) / 2:
            count = count + 1
    
    return count