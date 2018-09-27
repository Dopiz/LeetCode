def solution(X, Y, D):
    # write your code in Python 3.6
    step = (Y - X) // D
    return step if not (Y - X) % D else step + 1