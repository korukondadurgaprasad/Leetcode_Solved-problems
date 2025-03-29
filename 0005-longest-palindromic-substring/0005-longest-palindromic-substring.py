class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        
        if n <= 1:
            return s
        
        start = 0
        max_len = 1

        def expandAroundCenter(left, right):
            nonlocal start, max_len
            
            while left >= 0 and right < n and s[left] == s[right]:
                curr_len = right - left + 1
                if curr_len > max_len:
                    start = left
                    max_len = curr_len
                left -= 1
                right += 1

        for i in range(n):
            expandAroundCenter(i, i)
            expandAroundCenter(i, i + 1)
        
        return s[start:start + max_len]

            