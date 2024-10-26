class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if the target is at mid
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # Target not found, return the insertion point
        return left
            