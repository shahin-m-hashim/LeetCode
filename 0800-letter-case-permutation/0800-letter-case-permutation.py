class Solution(object):
    def letterCasePermutation(self, s):
        result = []

        # Helper function for backtracking
        def backtrack(substring, index):
            # Base case: If we reached the end, add to result
            if index == len(s):
                result.append(substring)
                return
            
            # If the current character is a digit, add it as is
            if s[index].isdigit():
                backtrack(substring + s[index], index + 1)
            else:
                # Explore both lowercase and uppercase transformations
                backtrack(substring + s[index].lower(), index + 1)
                backtrack(substring + s[index].upper(), index + 1)

        # Start backtracking from the first character
        backtrack("", 0)
        return result
