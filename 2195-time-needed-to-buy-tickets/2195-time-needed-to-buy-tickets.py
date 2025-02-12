class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        time = 0
        
        for i in range(len(tickets)):
            # If the person is before or at k, they buy up to tickets[k]
            if i <= k:
                time += min(tickets[i], tickets[k])
            # If the person is after k, they buy up to tickets[k] - 1
            else:
                time += min(tickets[i], tickets[k] - 1)
        
        return time