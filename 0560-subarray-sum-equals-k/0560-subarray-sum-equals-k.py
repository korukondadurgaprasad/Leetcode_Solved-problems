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
# https://chatgpt.com/share/684ef00e-27cc-8003-99dd-d7ed0e9f46fc


# def subarraySum(self, nums, k):
#     total = 0
#     cnt = 0
    
#     for i in range(len(nums)):
#         total = 0
        
#         for j in range(i, len(nums)):
#             total += nums[j]
            
#             if total == k:
#                 cnt += 1
    
#     return cnt
