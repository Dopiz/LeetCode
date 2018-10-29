def solution(N):
    # write your code in Python 3.6
    sqrt = max([i for i in range(1, int(N ** 0.5) + 1 ) if not N % i])
    
    return 2 * (sqrt + N // sqrt)