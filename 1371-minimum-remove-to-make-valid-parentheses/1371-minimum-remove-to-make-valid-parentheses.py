class Solution(object):
    def minRemoveToMakeValid(self, s):
        s = list(s)
        arr = []

        for i in range(len(s)):
            if s[i] == '(':
                arr.append(i)
            elif s[i] == ')':
                if arr:
                    arr.pop()
                else:
                    s[i] = ''

        for i in arr:
            s[i] = ''

        return ''.join(s)
