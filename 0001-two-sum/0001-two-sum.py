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

        #Using list we use .index menthod takes O(N2) TC


# The space complexity depends mainly on the space used by num_index_map,
#  which stores the elements of nums and their indices.
# Worst case: In the worst case, we will store all the numbers in the dictionary,
#  leading to space usage proportional to the number of elements in nums.
# Space Complexity: O(n)
