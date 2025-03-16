class Solution(object):
    def majorityElement(self, nums):
        cn1 = 0
        cn2 = 0
        ele1 = None
        ele2 = None

        # First pass: Find potential candidates
        for num in nums:
            if cn1 == 0 and num != ele2:
                cn1 = 1
                ele1 = num
            elif cn2 == 0 and num != ele1:
                cn2 = 1
                ele2 = num
            elif num == ele1:
                cn1 += 1
            elif num == ele2:
                cn2 += 1
            else:
                cn1 -= 1
                cn2 -= 1

        # Second pass: Verify the candidates
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == ele1:
                cnt1 += 1
            elif num == ele2:
                cnt2 += 1

        # Check if the counts are greater than n/3
        ls = []
        if cnt1 > len(nums) // 3:
            ls.append(ele1)
        if cnt2 > len(nums) // 3:
            ls.append(ele2)

        return ls
