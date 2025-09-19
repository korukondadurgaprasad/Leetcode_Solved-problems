class Solution(object):
    def removeKdigits(self, num, k):
        st = []
        for i in num:
            while st and k > 0 and st[-1] > i:
                st.pop()
                k -= 1
            st.append(i)

        # remove from the end if still k > 0
        while st and k > 0:
            st.pop()
            k -= 1

        if not st:
            return "0"

        res = ""
        while st:
            res += st.pop()

        # remove trailing zeros (which become leading zeros after reversing)
        res = res.rstrip('0')
        res = res[::-1]

        if not res:
            return "0"

        return res
