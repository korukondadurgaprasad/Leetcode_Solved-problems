class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        s=sum(nums)
        return n*(n+1)//2-s