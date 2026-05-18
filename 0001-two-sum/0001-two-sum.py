class Solution(object):
    def twoSum(self, nums, target):
        mapi={}
        for i in range(len(nums)):
            com=target - nums[i]
            if com in mapi:
                return [mapi[com],i]
            mapi[nums[i]]=i
