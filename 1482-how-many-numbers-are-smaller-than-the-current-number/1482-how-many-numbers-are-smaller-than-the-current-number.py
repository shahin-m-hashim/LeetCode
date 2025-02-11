class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        num_map = {}  
        sorted_nums = sorted(nums)

        for i, num in enumerate(sorted_nums):
            if num not in num_map:
                num_map[num] = i  
        
        return [num_map[num] for num in nums] 