from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum = 0
        count = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1
        
        for num in nums:
            prefix_sum += num
            
            if prefix_sum - k in sum_freq:
                count += sum_freq[prefix_sum - k]
            
            sum_freq[prefix_sum] += 1
        
        return count
