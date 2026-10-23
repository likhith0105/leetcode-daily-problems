class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper = {}
        last_lower = {}

        for i, c in enumerate(word):
            if c.islower():
                last_lower[c] = i
            else:
                c = c.lower()
                if c not in first_upper:
                    first_upper[c] = i

        return sum(
            c in last_lower and last_lower[c] < i
            for c, i in first_upper.items()
        )