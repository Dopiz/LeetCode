def solution(A):
    # write your code in Python 3.6
    cars = 0
    res = 0
    
    for num in A:
        if num == 0:
            cars = cars + 1
        else:
            res = res + cars
            if res > 1e9:
                return -1
    
    return res