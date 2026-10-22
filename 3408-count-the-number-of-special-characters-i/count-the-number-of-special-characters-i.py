class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_set = set(word)
        upper_set = set(word)
        
        count = 0
        for char in ascii_lowercase:
            if char in lower_set and char.upper() in upper_set:
                count += 1
                
        return count