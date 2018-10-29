def solution(A):
    # write your code in Python 3.6
    index = []
    for i in range(1, len(A) - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            index.append(i)
    
    if not index:
        return 0
        
    for i in range(len(index), 0, -1):
        
        if len(A) % i == 0:
            block = [0] * i
            block_size = len(A) // i
            
            for idx in index:
                if block[idx // block_size] == 0:
                    block[idx // block_size] = 1
        
            if all(block):
                return i
    
    return 0