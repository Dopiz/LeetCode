def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0
    
    max_ending = max_profit = 0
    for i in range(1, len(A)):
        max_ending = max(0, max_ending + A[i] - A[i - 1])
        max_profit = max(max_ending, max_profit)
    
    return max_profit