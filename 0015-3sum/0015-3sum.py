class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Sort the array first
        res = []  # Store unique triplets
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements
                continue
            
            left, right = i + 1, len(nums) - 1  # Two pointers
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]  # Sum of three numbers
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])  # Valid triplet
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:  # Skip duplicates
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:  # Skip duplicates
                        right -= 1
                
                elif total < 0:
                    left += 1  # Increase sum by moving left pointer
                else:
                    right -= 1  # Decrease sum by moving right pointer
        
        return res
