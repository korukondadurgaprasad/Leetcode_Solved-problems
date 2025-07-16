class Solution(object):
    def countGoodNumbers(self, n):
        MOD = 10**9 + 7

        even_count = (n + 1) // 2  # Positions: 0, 2, 4, ..., if n is odd
        odd_count = n // 2         # Positions: 1, 3, 5, ..., if n is >= 2

        return (pow(5, even_count, MOD) * pow(4, odd_count, MOD)) % MOD

        