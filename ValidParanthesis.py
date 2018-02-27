class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for x in s:
            if x != '}' and x != ')' and x != ']':
                stack = [x] + stack
            elif len(stack) != 0:
                if x == '}' and stack[0] == '{':
                    stack = stack[1:]
                elif x == ')' and stack[0] == '(':
                    stack = stack[1:]
                elif x == ']' and stack[0] == '[':
                    stack = stack[1:]
                else:
                    stack = [x] + stack
            else:
                stack = [x] + stack
                    
        if stack == []:
            return True
        else:
            return False