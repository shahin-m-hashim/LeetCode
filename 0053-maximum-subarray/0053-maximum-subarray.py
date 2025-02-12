class Solution(object):
    def maxSubArray(self, nums):
        dp = [0] * len(nums)

        for i, num in enumerate(nums):
            dp[i] = max(num, dp[i - 1] + num)            

        return max(dp)
