class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(n):
            # Check if current element is greater than the next (circularly)
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                
        # The array is valid if there is at most 1 drop
        return count <= 1