class Solution(object):
    def minSubArrayLen(self, target, nums):
        curr_sum=0
        l=0
        min_len=float('inf')
        for i in range(len(nums)):
            curr_sum+=nums[i]
            while curr_sum>=target:
                min_len=min(min_len,i-l+1)
                curr_sum-=nums[l]
                l+=1
        if min_len==float('inf'):
            return 0
        else:
            return min_len