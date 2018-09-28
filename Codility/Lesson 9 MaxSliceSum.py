def solution(A):
    # write your code in Python 3.6
    n = max_ending = max_slice = 0

    if all(num < 0 for num in A):
        n = max_ending = max_slice = -1000001

    for a in A:
        max_ending = max(n, max_ending + a, a)
        max_slice = max(max_slice, max_ending)
    
    return max_slice