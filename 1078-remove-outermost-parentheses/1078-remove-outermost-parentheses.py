class Solution(object):
    def removeOuterParentheses(self, s):
        res=[]
        cnt=0
        for char in s :
            if char =='(':
                if cnt>0:
                    res.append(char)
                cnt+=1
            else:
                cnt-=1
                if cnt>0:
                    res.append(char)
        return "".join(res)