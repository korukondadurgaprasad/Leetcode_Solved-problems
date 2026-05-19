class Solution(object):
    def minBitFlips(self, start, goal):
        num=start^goal
        cnt=0
        while num:
            num=num&(num-1)
            cnt+=1
        return cnt
        