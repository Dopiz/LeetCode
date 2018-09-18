def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    dict = {}
    for idx, num in enumerate(nums):
        t = target - num
        if t in dict:
            return [dict[t], idx]
        else:
            dict[num] = idx