class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        total_k = k1 + k2
        
        # Step 1: Compute absolute differences and store frequencies
        max_diff = 0
        diff_counts = [0] * 100001
        
        for i in range(n):
            d = abs(nums1[i] - nums2[i])
            if d > 0:
                diff_counts[d] += 1
                if d > max_diff:
                    max_diff = d
                    
        # Step 2: Greedily reduce the largest differences
        for d in range(max_diff, 0, -1):
            if diff_counts[d] == 0:
                continue
            
            # Number of operations needed to reduce all elements of difference `d` to `d - 1`
            ops_needed = diff_counts[d]
            
            if total_k >= ops_needed:
                total_k -= ops_needed
                diff_counts[d] = 0
                diff_counts[d - 1] += ops_needed
            else:
                # We can only reduce a portion of elements with difference `d`
                diff_counts[d] -= total_k
                diff_counts[d - 1] += total_k
                total_k = 0
                break
                
        # Step 3: Calculate the minimum sum of squared differences
        ans = 0
        for d in range(1, max_diff + 1):
            if diff_counts[d] > 0:
                ans += diff_counts[d] * (d ** 2)
                
        return ans