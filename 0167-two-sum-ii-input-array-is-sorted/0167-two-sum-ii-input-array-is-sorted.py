class Solution(object):
    def twoSum(self, nums, target):
        index_map = {} # num -> index
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return [index_map[complement] + 1, idx + 1]
            index_map[num] = idx
        return []
        