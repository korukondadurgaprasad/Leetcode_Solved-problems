class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        index = -1
        
        # Step 1: Find the break point
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
        
        # Step 2: If no break point, reverse the array
        if index == -1:
            nums.reverse()
            return nums
        
        # Step 3: Find the rightmost successor to swap
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break
        
        # Step 4: Reverse the elements to the right of the break point
        nums[index + 1:] = reversed(nums[index + 1:])
        
        return nums

