class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        b=x[::-1]
        if b==x:
            return True
        else:
            return False
        