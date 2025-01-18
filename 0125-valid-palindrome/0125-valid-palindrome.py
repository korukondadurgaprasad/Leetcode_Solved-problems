class Solution(object):
    def isPalindrome(self, s):
        a=''.join(c for c in s if c.isalnum()).lower()
        s=a[::-1]
        if a==s:
            return True
        else:
            return False
    
'''class Solution(object):
    def isPalindrome(self, s):
        # Initialize an empty string to store alphanumeric characters in lowercase
        cleaned_str = ''

        # Iterate through each character in the input string
        for char in s:
            # Check if the character is alphanumeric
            if char.isalnum():
                # Convert alphanumeric character to lowercase and append to cleaned_str
                cleaned_str += char.lower()

        # Compare the cleaned string with its reversed version
        return cleaned_str == cleaned_str[::-1]'''
