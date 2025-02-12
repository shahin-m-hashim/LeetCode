class Solution(object):
    def permute(self, nums):
        result = []

        # Helper function for recursion and backtracking
        def backtrack(start):
            # If we've reached the end, add a copy to the result
            if start == len(nums):
                result.append(nums[:])
                return
            
            # Swap each element with the current starting element
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap
                backtrack(start + 1)  # Recur for the next position
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack (swap back)

        # Start recursion from the first position
        backtrack(0)
        return result
