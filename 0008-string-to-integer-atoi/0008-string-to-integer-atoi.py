class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        sign = 1

        if s and s[0] == "-":
            sign = -1
            s = s[1:]
        elif s and s[0] == "+":
            s = s[1:]

        num = 0
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            else:
                break

        num = num * sign

        minn = -2**31
        maxx = 2**31 - 1

        if num > maxx:
            return maxx
        elif num < minn:
            return minn
        return num
