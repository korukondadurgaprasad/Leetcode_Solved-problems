class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxi = nums[0]  # Initialize maxi with the first element of the array
        sum = 0

        for i in range(n):
            sum += nums[i]

            if sum > maxi:
                maxi = sum

            # If sum < 0, discard the subarray and start fresh
            if sum < 0:
                sum = 0
        return maxi
            