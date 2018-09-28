import collections

def solution(A):
    # write your code in Python 3.6
    if not A:
        return -1

    # num = max(A, key=A.count)
    counter = collections.Counter(A).most_common(1)
    val = counter[0][0]
    cnt = counter[0][1]

    if cnt <= len(A) / 2:
        return -1
    
    return A.index(val)