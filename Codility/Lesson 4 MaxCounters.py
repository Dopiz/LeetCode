def solution(N, A):
    # write your code in Python 3.6
    res = [0] * N
    min_value = max_value = 0
    
    for num in A:
        idx = num - 1
        if idx == N:
            min_value = max_value
            continue
        res[idx] = max(res[idx], min_value) + 1
        max_value = max(res[idx], max_value)
    
    for i in range(N):
        res[i] = max(res[i], min_value)
        
    return res
            