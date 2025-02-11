class Solution(object):
    def longestMountain(self, arr):
        n = len(arr)
        max_length = 0
        i = 1  # Start from the second element

        while i < n - 1:
            # Check if arr[i] is a peak
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left, right = i, i

                # Expand left
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1
                
                # Expand right
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                
                # Update max length
                max_length = max(max_length, right - left + 1)

                # Move i to the end of the current mountain
                i = right  
            else:
                i += 1  # Move to the next element

        return max_length
