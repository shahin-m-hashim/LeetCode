class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        index_map = {}  # Store last index of each number
        
        for i, num in enumerate(nums):
            if num in index_map and (i - index_map[num]) <= k:
                return True  # Found a duplicate within k distance
            
            index_map[num] = i  # Update the last seen index
        
        return False
