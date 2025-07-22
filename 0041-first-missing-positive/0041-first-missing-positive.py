class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()

        # Add all positive numbers to the set
        for num in nums:
            if num > 0:
                num_set.add(num)

        # Start checking from 1 onwards
        i = 1
        while True:
            if i not in num_set:
                return i
            i += 1
