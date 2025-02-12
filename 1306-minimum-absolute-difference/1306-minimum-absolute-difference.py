class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()

        pairs = []
        min_diff = float('inf')
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            # If a new minimum is found, reset the result list
            if diff < min_diff:
                min_diff = diff
                pairs = [[arr[i], arr[i + 1]]]
            
            # If the same minimum is found, append the pair
            elif diff == min_diff:
                pairs.append([arr[i], arr[i + 1]])
        
        return pairs


        