def solution(A, K):
    # write your code in Python 3.6
    if not A:
        return A
    K = K % len(A)
    return A[len(A) - K:] + A[:len(A) - K]