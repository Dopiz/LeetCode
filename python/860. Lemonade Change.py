def lemonadeChange(self, bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    five = 0
    ten  = 0
    for num in bills:
        if num == 5:
            five = five + 1
        elif num == 10:
            five = five - 1
            ten = ten + 1
        elif num == 20:
            five = five - 1 if ten else five - 3
            ten = ten - 1 if ten else ten
        
        if five < 0: return False

    return True