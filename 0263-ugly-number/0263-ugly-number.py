class Solution(object):
    def isUgly(self, n):
        if (n <= 0):
            return false; 
        cons = [2, 3, 5]
        for i in cons:
            while (n % i == 0): 
                n /= i
        return n == 1;
        