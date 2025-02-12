class NumArray(object):
    def __init__(self, nums):
        # Initialize the prefix sum array
        self.prefix = [0] * (len(nums) + 1)
        
        # Compute the prefix sum
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left, right):
        # Return the sum of the subarray from left to right
        return self.prefix[right + 1] - self.prefix[left]
