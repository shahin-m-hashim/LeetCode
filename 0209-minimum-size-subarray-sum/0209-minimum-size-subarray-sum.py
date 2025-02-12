class Solution(object):
    def minSubArrayLen(self, target, nums):
        Sum = 0
        left = 0
        min_len = float('inf')

        for right in range(len(nums)):
            Sum += nums[right]  # Expand the window
            
            # Shrink the window as small as possible while the sum is >= target
            while Sum >= target:
                min_len = min(min_len, right - left + 1)
                Sum -= nums[left]  # Shrink the window
                left += 1

        # If no valid subarray was found, return 0
        return min_len if min_len != float('inf') else 0
