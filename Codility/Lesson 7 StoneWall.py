def solution(H):
    # write your code in Python 3.6
    stone = 0
    stack = []
    
    for h in H:
        while stack and stack[-1] > h:
            stack.pop()
        if stack and h == stack[-1]:
            continue
        stack.append(h)
        stone = stone + 1
        
    return stone