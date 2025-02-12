class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()

        min_diff = float('inf')
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        pairs = []
        for i in range(len(arr) - 1):
            if(arr[i + 1] - arr[i] == min_diff):
                pairs.append([arr[i], arr[i + 1]])
        
        return pairs


        