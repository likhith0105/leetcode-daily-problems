class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def get_digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        # Pair each number with its original index and digit sum
        indexed_nums = []
        for i, val in enumerate(nums):
            indexed_nums.append((get_digit_sum(val), val, i))
            
        # Sort by digit sum, then by value
        indexed_nums.sort(key=lambda x: (x[0], x[1]))
        
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or indexed_nums[i][2] == i:
                continue
                
            # Traverse the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = indexed_nums[curr][2]
                cycle_size += 1
                
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        # Alternatively, swaps = n - number_of_cycles
        return swaps