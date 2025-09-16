class Solution(object):
    def findContentChildren(self, g, s):
        n=len(g)
        m=len(s)
        l=0
        r=0
        s.sort()
        g.sort()
        while l<m and r<n:
            if s[l]>=g[r]:
                r+=1
            l+=1
        return r
            