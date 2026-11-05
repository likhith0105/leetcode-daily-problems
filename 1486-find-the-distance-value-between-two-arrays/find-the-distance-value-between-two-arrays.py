from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        distance_count = 0
        
        for x in arr1:
            idx = bisect_left(arr2, x)
            valid = True
            
            # Check the closest element to the right, if it exists
            if idx < len(arr2) and abs(arr2[idx] - x) <= d:
                valid = False
            # Check the closest element to the left, if it exists
            if idx > 0 and abs(arr2[idx - 1] - x) <= d:
                valid = False
                
            if valid:
                distance_count += 1
                
        return distance_count