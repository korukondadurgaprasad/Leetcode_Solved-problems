class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        minOpen = 0  # smallest possible number of '('
        maxOpen = 0  # largest possible number of '('

        for c in s:
            if c == '(':
                minOpen += 1
                maxOpen += 1
            elif c == ')':
                minOpen -= 1
                maxOpen -= 1
            else:  # c == '*'
                # '*' can be treated as ')' for minOpen
                minOpen -= 1
                # '*' can be treated as '(' for maxOpen
                maxOpen += 1

            # If at any time maxOpen < 0, too many ')'
            if maxOpen < 0:
                return False

            # minOpen can’t be negative (we can treat '*' as '(')
            if minOpen < 0:
                minOpen = 0

        # Valid if at the end, all '(' can be matched
        return minOpen == 0


        