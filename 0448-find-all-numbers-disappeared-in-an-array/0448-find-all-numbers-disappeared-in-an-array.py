class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1  # Get correct index
            nums[index] = -abs(nums[index])  # Mark as visited
        
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

        