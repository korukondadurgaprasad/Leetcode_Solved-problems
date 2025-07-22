class Solution(object):
    def countGoodSubstrings(self, s):
        l=0
        dic={}
        cnt=0
        k=3
        for r in range(len(s)):
            if s[r] in dic:
                dic[s[r]]+=1
            else:
                dic[s[r]]=1
            if r-l==k:
                dic[s[l]]-=1
                if dic[s[l]]==0:
                    dic.pop(s[l])
                l+=1
            if len(dic)==k:
                cnt+=1
        return cnt






        # st=set()
        # count=0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         res=s[i:j+1]
        #         if len(res)==3 and len(set(res))==3:
        #             count+=1
        # return count
        