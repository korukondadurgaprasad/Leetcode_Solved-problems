import heapq

class Solution(object):
    def minimumDifference(self, nums):
        n = len(nums) // 3
        
        # Prefix: max sum from left to mid using smallest n elements
        left_heap = []
        left_sum = 0
        left_sums = [0] * (2 * n + 1)

        for i in range(2 * n):
            heapq.heappush(left_heap, -nums[i])
            left_sum += nums[i]
            if len(left_heap) > n:
                left_sum += heapq.heappop(left_heap)
            if len(left_heap) == n:
                left_sums[i] = left_sum

        # Suffix: min sum from right to mid using largest n elements
        right_heap = []
        right_sum = 0
        right_sums = [0] * (2 * n + 1)

        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(right_heap, nums[i])
            right_sum += nums[i]
            if len(right_heap) > n:
                right_sum -= heapq.heappop(right_heap)
            if len(right_heap) == n:
                right_sums[i] = right_sum

        # Find minimum difference
        res = float('inf')
        for i in range(n - 1, 2 * n):
            if left_sums[i] and right_sums[i + 1]:
                res = min(res, left_sums[i] - right_sums[i + 1])

        return res
