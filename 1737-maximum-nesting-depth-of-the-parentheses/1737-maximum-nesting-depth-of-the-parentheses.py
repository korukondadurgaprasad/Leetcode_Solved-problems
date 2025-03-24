class Solution(object):
    def maxDepth(self, s):
        depth=0
        max_d=0
        for i in s:
            if i=='(':
                depth+=1
                max_d=max(max_d,depth)
            elif i==')':
                depth-=1
        return max_d