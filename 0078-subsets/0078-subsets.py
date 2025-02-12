class Solution(object):
    def subsets(self, nums):
        subsets = [[]]
        for num in nums:
            subset = [curr + [num] for curr in subsets]
            subsets.extend(subset)
        
        return subsets
