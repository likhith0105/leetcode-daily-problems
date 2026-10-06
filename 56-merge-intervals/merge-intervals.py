class Solution:

  def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    # 1. Sort the intervals based on their start time
    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
      # If 'merged' is empty or no overlap with the last merged interval, append it
      if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
      else:
        # Overlap exists; merge by updating the end time of the last interval
        merged[-1][1] = max(merged[-1][1], interval[1])

    return merged