class Solution(object):
    def combine(self, n, k):
        result = []

        # Helper function for recursion and backtracking
        def backtrack(start, combination):
            # If the combination is of length k, add to result
            if len(combination) == k:
                result.append(combination[:])
                return
            
            # Start from the current number and go up to n
            for i in range(start, n + 1):
                combination.append(i)  # Include the current number
                backtrack(i + 1, combination)  # Recur with next number
                combination.pop()  # Backtrack and remove the last number
        
        # Start recursion with the first number
        backtrack(1, [])
        return result
