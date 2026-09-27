class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters until matching '(' is found
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the opening parenthesis '('
                stack.pop()
                # Push the reversed characters back onto stack
                stack.extend(temp)
            else:
                stack.append(char)
                
        return "".join(stack)