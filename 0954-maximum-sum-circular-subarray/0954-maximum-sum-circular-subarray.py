class Solution(object):
    def maxSubarraySumCircular(self, nums):
        
        total=0
        culmax=0
        culmin=0
        golmax,golmin=nums[0],nums[0]
        for n in nums:
            culmax=max(culmax+n,n)
            culmin=min(culmin+n,n)
            total+=n
            golmax=max(golmax,culmax)
            golmin=min(golmin,culmin)
        if golmax>0:
            return max(golmax,total-golmin)
        else:
           return golmax


        