class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        res = []
        for num in range(2**n):  # Outer loop variable should be 'num'
            sub = []
            for i in range(n):   # Inner loop variable is 'i'
                if (num >> i) & 1:
                    sub.append(nums[i])
            res.append(sub)
        return res
