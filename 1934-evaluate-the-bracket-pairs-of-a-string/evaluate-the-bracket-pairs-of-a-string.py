class Solution:

    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {k: v for k, v in knowledge}
        res = []
        i = 0
        n = len(s)

        while i < n:
            if s[i] == "(":
                j = i + 1
                while s[j] != ")":
                    j += 1
                key = s[i + 1 : j]
                res.append(d.get(key, "?"))
                i = j + 1
            else:
                res.append(s[i])
                i += 1

        return "".join(res)