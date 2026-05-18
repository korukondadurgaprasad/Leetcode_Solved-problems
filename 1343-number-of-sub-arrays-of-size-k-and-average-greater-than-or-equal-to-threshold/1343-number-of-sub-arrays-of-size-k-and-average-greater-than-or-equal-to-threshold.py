class Solution(object):

    def numOfSubarrays(self, arr, k, threshold):

        count = 0

        l = 0
        sumi = 0

        for i in range(len(arr)):

            sumi += arr[i]

            # Maintain window size
            if i - l + 1 > k:

                sumi -= arr[l]
                l += 1

            # Window size becomes k
            if i - l + 1 == k:

                if sumi / float(k) >= threshold:

                    count += 1

        return count