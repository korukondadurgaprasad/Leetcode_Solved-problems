class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n  # Step 1: Initialize result with 1s

        prefix = 1
        # Step 2: Fill result with prefix products (left side)
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        # Step 3: Multiply result with suffix products (right side)
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
