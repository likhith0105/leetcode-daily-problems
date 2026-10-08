class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to easily skip duplicate elements
        res = []

        def backtrack(start_idx, current_combination, current_sum):
            if current_sum == target:
                res.append(list(current_combination))
                return
            
            for i in range(start_idx, len(candidates)):
                # Skip duplicate elements at the same recursion level
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                
                # Prune tree if the candidate exceeds the remaining target
                if current_sum + candidates[i] > target:
                    break

                current_combination.append(candidates[i])
                # Move to the next element (`i + 1`) because each number can only be used once
                backtrack(i + 1, current_combination, current_sum + candidates[i])
                current_combination.pop()

        backtrack(0, [], 0)
        return res