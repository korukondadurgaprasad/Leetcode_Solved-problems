class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        st={}
        ts={}
        for i in range(len(s)):
            c1=s[i]
            c2=t[i]
            if c1 in st:
                if st[c1]!=c2:
                    return False
            elif c2 in ts:
                if ts[c2]!=c1:
                    return False

            else:
                st[c1]=c2
                ts[c2]=c1
        return True