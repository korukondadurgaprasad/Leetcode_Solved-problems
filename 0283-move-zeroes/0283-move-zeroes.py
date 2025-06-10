class Solution(object):
    def moveZeroes(self, nums):

        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        while j<len(nums):
            nums[j]=0
            j+=1
        return nums


    #     def moveZeroes(nums):
    # result = [num for num in nums if num != 0]  # Collect all non-zero elements
    # result.extend([0] * (len(nums) - len(result)))  # Append the required number of zeroes
    # return result