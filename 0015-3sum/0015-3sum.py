class Solution(object):
    def threeSum(self, nums):
        ans=set()
        for i in range(len(nums)):
            st=set()
            for j in range(i+1,len(nums)):
                third=-(nums[i]+nums[j])
                if third in st:
                    temp=[nums[i],nums[j],third]
                    temp.sort()
                    ans.add(tuple(temp))
                st.add(nums[j])
        res=list(ans)
        return res
                
