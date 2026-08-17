class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if (c == '[' or c == '{' or c== '('):
                stack.append(c)
            if (c == ']' or c == '}' or c== ')'):
                if not stack:
                    return False
                if((stack)[-1] == '(' and c!= ')'):
                    return False
                if((stack)[-1] == '[' and c!= ']'):
                    return False    
                if((stack)[-1] == '{' and c!= '}'):
                    return False
                stack.pop()
        return not stack