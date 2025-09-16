class Solution(object):
    def jump(self, nums):
        jumps = 0
        l = 0
        r = 0
        while r < len(nums) - 1:
            farthest = 0
            # explore all indices in current level [l, r]
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            # move to next level
            l = r + 1
            r = farthest
            jumps += 1
        return jumps

        