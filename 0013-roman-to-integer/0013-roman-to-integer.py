class Solution(object):
    def romanToInt(self, s):
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
               'C': 100, 'D': 500, 'M': 1000}
        total = 0
        length = len(s)
        
        for i in range(length):
            # Check if the current numeral is less than the next numeral
            if i <length-1 and rom[s[i]] <rom[s[i + 1]]:
                total -= rom[s[i]]
            else:
                total += rom[s[i]]
                
        return total
