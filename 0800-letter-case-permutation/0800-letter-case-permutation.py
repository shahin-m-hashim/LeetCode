class Solution(object):
    def letterCasePermutation(self, s):
        res = []

        def backtrack(sub = "", i = 0):
            if len(sub) == len(s):
                res.append(sub)
            else:
                if s[i].isalpha():
                    backtrack(sub + s[i].swapcase(), i + 1)
                backtrack(sub + s[i], i + 1)

        backtrack()
        return res
