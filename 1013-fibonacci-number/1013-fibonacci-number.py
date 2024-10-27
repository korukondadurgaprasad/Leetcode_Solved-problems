class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a = 0
        b = 1
        for i in range(2, n + 1):  # Loop n - 1 times, starting from 2 up to n
            c = a + b
            a = b
            b = c
        return b

        