class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        
        # Case 1: Change two smallest elements -> new min is nums[2], max is nums[-1]
        opt1 = nums[-1] - nums[2]
        
        # Case 2: Change two largest elements -> new min is nums[0], max is nums[-3]
        opt2 = nums[-3] - nums[0]
        
        # Case 3: Change one smallest and one largest -> new min is nums[1], max is nums[-2]
        opt3 = nums[-2] - nums[1]
        
        return min(opt1, opt2, opt3)