#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> fourSum(std::vector<int>& nums, int target) {
        std::vector<std::vector<int>> ans;
        int n = nums.size();
        if (n < 4) return ans;

        // 1. Sort the array
        std::sort(nums.begin(), nums.end());

        // 2. Fix the first element
        for (int i = 0; i < n - 3; ++i) {
            // Avoid duplicate quadruplets for the first position
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            // Pruning: Smallest possible 4-sum is too large
            if ((long long)nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target) break;
            // Pruning: Largest possible 4-sum with this nums[i] is too small
            if ((long long)nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target) continue;

            // 3. Fix the second element
            for (int j = i + 1; j < n - 2; ++j) {
                // Avoid duplicate quadruplets for the second position
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                // Pruning for the second loop
                if ((long long)nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target) break;
                if ((long long)nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target) continue;

                // 4. Two-pointer approach for the remaining two elements
                int left = j + 1;
                int right = n - 1;

                while (left < right) {
                    long long sum = (long long)nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum == target) {
                        ans.push_back({nums[i], nums[j], nums[left], nums[right]});

                        // Skip duplicates for the third and fourth elements
                        while (left < right && nums[left] == nums[left + 1]) left++;
                        while (left < right && nums[right] == nums[right - 1]) right--;

                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return ans;
    }
};