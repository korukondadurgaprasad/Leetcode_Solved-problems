class Solution(object):
    def findErrorNums(self, nums):
        a=sum(nums)-sum(set(nums))
        b=sum(range(1,len(nums)+1))-sum(set(nums))
        return [a,b]
'''class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        op = [0, 0]
        for i in range(1, len(nums) + 1):
            if counts[i] == 2:
                op[0] = i
            if counts[i] == 0:
                op[1] = i
        return op
'''