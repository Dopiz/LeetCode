def solution(S):
    # write your code in Python 3.6
    if len(S) % 2:
        return 0
        
    m = {']': '[', '}': '{', ')': '('}
    stack = []
    for s in S:
        if s in m:
            if not stack or (stack and stack.pop() != m[s]):
                return 0
        else:
            stack.append(s)
            
    return 1 if not stack else 0