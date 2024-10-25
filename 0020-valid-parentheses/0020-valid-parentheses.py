class Solution(object):
    def isValid(self, s):
        stack = []
    
        for char in s:
            # If it's an opening bracket, push the corresponding closing bracket onto the stack
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            # If it's a closing bracket, check if it matches the top of the stack
            elif not stack or stack.pop() != char:
                return False
        
        # If the stack is empty, the string is valid
        return len(stack) == 0

            