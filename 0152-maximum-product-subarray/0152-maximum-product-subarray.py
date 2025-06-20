class Solution(object):
    def maxProduct(self, nums):
        preff=1
        suff=1
        ans = float('-inf')
        for i in range(len(nums)):
            if preff==0:
                preff=1
            if suff==0:
                suff=1
            preff*=nums[i]
            suff*=nums[len(nums)-1-i]
            ans=max(ans,max(preff,suff))
        return ans
        