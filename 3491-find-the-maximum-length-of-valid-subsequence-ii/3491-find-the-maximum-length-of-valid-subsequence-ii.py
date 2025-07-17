from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        max_len = 1  # minimum length is 1

        for j in range(n):
            for i in range(j):
                mod = (nums[i] + nums[j]) % k
                dp[j][mod] = max(dp[j][mod], dp[i][mod] + 1)
                max_len = max(max_len, dp[j][mod] + 1)

        return max_len
