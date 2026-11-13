from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        cost = 0
        dq = deque()  # stores tuples of (num, count)
        j = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            count = 1
            
            # Maintain a monotonic non-increasing stack/deque from right to left
            while dq and dq[-1][0] < num:
                next_num, next_count = dq.pop()
                count += next_count
                cost += (num - next_num) * next_count
            
            dq.append((num, count))
            
            # Shrink the window from the right if the operation cost exceeds k
            while cost > k:
                rightmost_num, rightmost_count = dq.popleft()
                cost -= (rightmost_num - nums[j])
                j -= 1
                if rightmost_count > 1:
                    dq.appendleft((rightmost_num, rightmost_count - 1))
            
            ans += j - i + 1
            
        return ans