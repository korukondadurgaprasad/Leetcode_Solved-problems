class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        
        l = 0
        cntT = 0
        cntF = 0
        ans = 0

        for r in range(len(answerKey)):

            if answerKey[r] == "T":
                cntT += 1
            else:
                cntF += 1

            while min(cntT, cntF) > k:

                if answerKey[l] == "T":
                    cntT -= 1
                else:
                    cntF -= 1

                l += 1

            ans = max(ans, r - l + 1)

        return ans