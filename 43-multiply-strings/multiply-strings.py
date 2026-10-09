class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # The product of a length m number and length n number has at most m + n digits
        res = [0] * (m + n)
        
        # Multiply digit by digit from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                
                # Add product to current position and propagate carry
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10
        
        # Convert result array to string, skipping leading zeros
        result_str = "".join(map(str, res))
        return result_str.lstrip("0")