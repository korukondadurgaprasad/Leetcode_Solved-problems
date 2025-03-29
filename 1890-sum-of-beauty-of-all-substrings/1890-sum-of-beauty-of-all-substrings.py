class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty=0
        for i in range(len(s)):
            fr={}
            for j in range(i,len(s)):
                char=s[j]
                fr[char]=fr.get(char,0)+1
                max_freq = max(fr.values())
                min_freq = min(fr.values())
                beauty = max_freq - min_freq
                total_beauty += beauty
        return total_beauty