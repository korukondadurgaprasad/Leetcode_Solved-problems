class Solution(object):
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        if n == 1:
            return 1  # only one element

        res = 1  # final answer
        l = 0    # left side of window
        prev = ""  # stores last sign ('<' or '>')

        for r in range(1, n):
            # Compare current pair
            if arr[r-1] > arr[r]:
                curr = ">"
            elif arr[r-1] < arr[r]:
                curr = "<"
            else:
                curr = "="

            if curr == "=":
                # If equal elements, reset the window
                l = r
                prev = ""
            elif curr == prev:
                # If same sign repeated, reset window from previous element
                l = r - 1
                prev = curr
            else:
                # Pattern changed: update max length
                res = max(res, r - l + 1)
                prev = curr

        return res



        