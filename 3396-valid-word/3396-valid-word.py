class Solution(object):
    def isValid(self, word):
        if len(word) < 3:
            return False
        
        vowels = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False
        
        for ch in word:
            if not ch.isalnum():  # not a letter or digit
                return False
            if ch.isalpha():  # it's a letter
                if ch in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
        
        return has_vowel and has_consonant
