class Solution:

    def minOperations(self, grid: list[list[int]], x: int) -> int:
        # Flatten the 2D grid into a 1D list
        nums = [num for row in grid for num in row]

        # All elements must have the same remainder modulo x to be convertible
        rem = nums[0] % x
        for num in nums:
            if num % x != rem:
                return -1

        # Sort elements to find the median target value
        nums.sort()
        median = nums[len(nums) // 2]

        # Sum the operations required to make each element equal to the median
        return sum(abs(num - median) // x for num in nums)