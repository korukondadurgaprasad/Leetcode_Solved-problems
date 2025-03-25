class Solution(object):
    def myAtoi(self, s):
        s=s.strip()
        if not s:
            return 0
        sign=1
        if s[0]=='-':
            sign=-1
            s=s[1:]
        elif s[0]=='+':
            s=s[1:]

        num=0
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            else:
                break
        num*=sign
        maxi=2**31-1
        mini=-2**31
        if num > maxi:
            return maxi
        elif num<mini:
            return mini
        return num