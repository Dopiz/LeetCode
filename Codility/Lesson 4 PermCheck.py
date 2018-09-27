def solution(A):
    # write your code in Python 3.6
    B = set(A)
    return 1 if max(B) == len(B) and len(B) == len(A) else 0