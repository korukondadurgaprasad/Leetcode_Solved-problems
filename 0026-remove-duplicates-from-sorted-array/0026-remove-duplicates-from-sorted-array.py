class Solution(object):
    def removeDuplicates(self,nums):
        if not nums:
            return 0  # If the list is empty, return 0

        # Start with the first element
        k = 1  # Position for the next unique element
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Check if the current element is different from the previous one
                nums[k] = nums[i]  # Place the unique element at position k
                k += 1  # Move the position for the next unique element

        return k  # Return the count of unique elements

        