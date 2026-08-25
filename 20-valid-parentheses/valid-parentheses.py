class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_brackets = {')':'(', '}':'{',']':'['}
        for char in s :
            if char in dict_brackets:
                if stack and stack[-1] == dict_brackets[char]:
                    stack.pop()
                else : 
                    return False 
            else : 
                stack.append(char)
        return not stack