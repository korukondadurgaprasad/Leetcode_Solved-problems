class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            sin=nums.count(i)
            if sin==1:
                return i
                



        