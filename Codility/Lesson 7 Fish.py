def solution(A, B):
    # write your code in Python 3.6
    fish = 0
    stack = []
    
    for i in range(len(A)):
        if B[i] == 1:
            stack.append(A[i])
        else:
            while stack:
                if A[i] > stack[-1]:
                    stack.pop()
                else:
                    break
                
            if not stack:
                fish = fish + 1
            
    return fish + len(stack)
                    