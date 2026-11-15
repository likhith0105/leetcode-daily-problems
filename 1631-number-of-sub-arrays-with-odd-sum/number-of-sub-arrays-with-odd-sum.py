class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  # Base case: prefix sum 0 is even
        current_sum = 0
        total_subarrays = 0
        
        for num in arr:
            current_sum += num
            
            if current_sum % 2 == 1:
                total_subarrays += even_count
                odd_count += 1
            else:
                total_subarrays += odd_count
                even_count += 1
                
        return total_subarrays % MOD