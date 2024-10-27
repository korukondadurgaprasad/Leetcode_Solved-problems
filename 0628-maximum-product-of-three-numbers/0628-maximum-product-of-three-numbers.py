class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        threeLowToHigh=nums[-1] * nums[-2] * nums[-3]
        threeHighToLow=nums[0] * nums[1] * nums[-1]
        maxOfThree=max(threeLowToHigh, threeHighToLow)
        
        return maxOfThree
