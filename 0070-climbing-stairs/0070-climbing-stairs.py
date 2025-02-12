class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        one_step_before = 2  # ways(2)
        two_steps_before = 1 # ways(1)
        
        for i in range(3, n + 1):
            current = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = current
        
        return one_step_before
