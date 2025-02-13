class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0
        
        # Phase 1: Find the majority candidate
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        
        # Phase 2: Verify the candidate (Optional since the problem guarantees a majority element)
        c=0
        for i in range(len(nums)):
            if nums[i]==candidate:
                c+=1
        if c > len(nums) // 2:
            return candidate
        return None  # This line will not be reached if a majority element is guaranteed


            