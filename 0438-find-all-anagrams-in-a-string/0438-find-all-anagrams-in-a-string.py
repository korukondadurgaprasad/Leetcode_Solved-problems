from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        len_p = len(p)
        len_s = len(s)

        if len_s < len_p:
            return res

        p_counter = Counter(p)
        s_counter = Counter(s[:len_p])  # First window

        for i in range(len_s - len_p):
            if s_counter == p_counter:
                res.append(i)

            # Remove the leftmost character from window
            s_counter[s[i]] -= 1
            if s_counter[s[i]] == 0:
                del s_counter[s[i]]

            # Add the next character directly
            s_counter[s[i + len_p]] += 1

        # Final check for the last window
        if s_counter == p_counter:
            res.append(len_s - len_p)

        return res
