import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of numbers from 1 to n
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Convert k to 0-based index
        k -= 1
        
        permutation = []
        
        for i in range(n, 0, -1):
            # Calculate the factorial of (i - 1)
            fact = math.factorial(i - 1)
            
            # Find the index of the current digit
            index = k // fact
            
            # Append the chosen digit to our result list
            permutation.append(numbers.pop(index))
            
            # Update k for the next iteration
            k %= fact
            
        return "".join(permutation)