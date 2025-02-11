class Solution(object):
    def sortedSquares(self, nums):
        squared = [n ** 2 for n in nums]
        squared.sort()
        return squared
        