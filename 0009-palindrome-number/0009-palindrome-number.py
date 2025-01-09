class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        b=x[::-1]
        if b==x:
            return True
        else:
            return False
        