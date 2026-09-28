class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(open_count: int, close_count: int, current_str: str):
            # Base case: if the current string length equals 2 * n, we've formed a valid combination
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # Can add an open parenthesis if we haven't reached n open parentheses
            if open_count < n:
                backtrack(open_count + 1, close_count, current_str + "(")
                
            # Can add a close parenthesis if open count > close count (maintains validity)
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_str + ")")
                
        backtrack(0, 0, "")
        return result