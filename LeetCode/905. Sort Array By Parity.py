def sortArrayByParity(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    even_nums = [num for num in A if num % 2 == 0]
    odd_nums = [num for num in A if num % 2 == 1]
    
    return even_nums + odd_nums