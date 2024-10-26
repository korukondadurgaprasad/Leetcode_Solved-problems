class Solution(object):
    def lengthOfLastWord(self, s):
        b=s.strip().split(" ")
        length=len(b[-1])
        return length
        