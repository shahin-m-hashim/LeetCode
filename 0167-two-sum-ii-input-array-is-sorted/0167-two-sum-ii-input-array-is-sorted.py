class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1  # Two-pointer approach
        
        while left < right:
            total = numbers[left] + numbers[right]
            
            if total == target:
                return [left + 1, right + 1]  # Convert to 1-based indexing
            elif total < target:
                left += 1  # Increase sum by moving left pointer
            else:
                right -= 1  # Decrease sum by moving right pointer
