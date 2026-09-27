class Solution:

  def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []

    for i in range(len(nums) - 2):
      # Since array is sorted, if first element is > 0, sum cannot be 0
      if nums[i] > 0:
        break

      # Skip duplicate values for the first element
      if i > 0 and nums[i] == nums[i - 1]:
        continue

      left, right = i + 1, len(nums) - 1

      while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total < 0:
          left += 1
        elif total > 0:
          right -= 1
        else:
          res.append([nums[i], nums[left], nums[right]])

          # Skip duplicate values for second and third elements
          while left < right and nums[left] == nums[left + 1]:
            left += 1
          while left < right and nums[right] == nums[right - 1]:
            right -= 1

          left += 1
          right -= 1

    return res