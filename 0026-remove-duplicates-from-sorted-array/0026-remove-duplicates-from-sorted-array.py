class Solution(object):
    def removeDuplicates(self, nums):
        k=0
        for i in range(0,len(nums)):
            if i==len(nums)- 1 or nums[i]!=nums[i+1]:
                nums[k]=nums[i]
                k+=1
        return k
        