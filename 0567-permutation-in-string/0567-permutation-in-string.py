from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)

        if len1 > len2:
            return False

        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len1])  # Initial window

        for i in range(len2 - len1):
            if s1_counter == s2_counter:
                return True

            # Remove the left character
            s2_counter[s2[i]] -= 1
            if s2_counter[s2[i]] == 0:
                del s2_counter[s2[i]]

            # Add the right character
            s2_counter[s2[i + len1]] += 1

        # Final window check
        if s1_counter == s2_counter:
            return True

        return False

        