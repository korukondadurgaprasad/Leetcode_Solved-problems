class Solution(object):

    def minimumDifference(self, nums, k):

        nums.sort()

        l = 0
        n = len(nums)

        mini = float("inf")

        for r in range(n):

            if r - l == k:
                l += 1

            if r - l + 1 == k:

                mini = min(mini, nums[r] - nums[l])

        return mini