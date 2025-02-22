class Solution(object):
    def rearrangeArray(self, nums):
        pos=0
        neg=1
        res=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                res[pos]=nums[i]
                pos+=2
            else:
                res[neg]=nums[i]
                neg+=2
        return res
        # n=len(nums)
        # pos=[]
        # neg=[]
        # for i in range(n):
        #     if nums[i]>0:
        #         pos.append(nums[i])
        #     else:
        #         neg.append(nums[i])
        # for i in range(n/2):
        #     nums[2*i]=pos[i]
        #     nums[2*i+1]=neg[i]
        # return nums
            
        