class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_exponent = False
        seen_dot = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in "+-":
                # Sign is only valid at the beginning or right after an exponent
                if i > 0 and s[i - 1] not in "eE":
                    return False
            elif char in ".":
                # A dot is invalid if we already saw a dot or an exponent
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            elif char in "eE":
                # An exponent is invalid if we already saw one, or if no digits appeared before it
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False  # Reset to ensure digits follow the exponent
            else:
                return False
                
        return seen_digit