def solution(A):
    # write your code in Python 3.6
    # return int(sum(range(len(A) + 2)) - sum(A))
    return int((1 + len(A) + 1) * (len(A) + 1) / 2 - sum(A))