class Solution(object):
    def twoSum(self, nums, target):

        # ---O(N2)--
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return i,j     
        # ---O(N)--
        num_index_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_index_map:
                return [num_index_map[complement], i]

            num_index_map[nums[i]] = i
        return []