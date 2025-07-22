class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        num_set = set(nums)  # Store all nums for O(1) lookups
        count = 0

        for num in nums:  # Loop over nums in order
            if (num + diff) in num_set and (num + 2 * diff) in num_set:
                count += 1

        return count
