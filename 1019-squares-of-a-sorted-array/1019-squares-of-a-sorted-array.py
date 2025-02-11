class Solution(object):
    def sortedSquares(self, nums):
        l, r = 0, len(nums) - 1  # Two pointers
        result = [0] * len(nums)  # Output array (same size as input)
        k = len(nums) - 1  # Start filling from the right
        
        while l <= r:
            left_sq = nums[l] ** 2
            right_sq = nums[r] ** 2
            
            if left_sq > right_sq:
                result[k] = left_sq
                l += 1  # Move left pointer forward
            else:
                result[k] = right_sq
                r -= 1  # Move right pointer backward
                
            k -= 1  # Move to the next position in result
            
        return result
