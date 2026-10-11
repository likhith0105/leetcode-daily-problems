class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We don't need to visit the last index because 
        # the jump would already land on or beyond it.
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest
                
        return jumps