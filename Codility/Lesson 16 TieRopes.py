def solution(K, A):
    # write your code in Python 3.6
    count = max_ending = 0

    for a in A:
        
        if a >= K:
            count = count + 1
            max_ending = 0
        else:
            max_ending = max_ending + a

        if max_ending >= K:
            count = count + 1
            max_ending = 0

    return count