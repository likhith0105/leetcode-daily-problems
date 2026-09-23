class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        
        # If the total sum is less than x, it's impossible
        if target < 0:
            return -1
        
        # If total sum equals x, we must remove all elements
        if target == 0:
            return len(nums)
        
        # Sliding window to find the longest subarray with sum == target
        left = 0
        current_sum = 0
        max_len = -1
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink window if current_sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # Update max_len if target sum is found
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
        
        return len(nums) - max_len if max_len != -1 else -1