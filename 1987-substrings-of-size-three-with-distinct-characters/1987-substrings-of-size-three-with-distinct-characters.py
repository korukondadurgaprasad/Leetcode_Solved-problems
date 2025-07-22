class Solution(object):
    def countGoodSubstrings(self, s):
        st=set()
        count=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                res=s[i:j+1]
                if len(res)==3 and len(set(res))==3:
                    count+=1
        return count
        