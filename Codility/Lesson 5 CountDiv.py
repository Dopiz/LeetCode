def solution(A, B, K):
    # write your code in Python 3.6
    A = (A + K - 1) // K * K
    return (B - A) // K + 1