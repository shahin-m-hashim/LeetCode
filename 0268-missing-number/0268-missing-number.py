class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for n in range(len(nums) + 1):
            if n not in nums:
                return n
        
        return -1