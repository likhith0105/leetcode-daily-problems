class Solution:

  def minimumCost(
      self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
  ) -> int:
    # Handle overlap using type 3 items or individual items
    common = min(need1, need2)
    total_cost = common * min(costBoth, cost1 + cost2)

    # Remaining needs for type 1 and type 2
    rem1 = need1 - common
    rem2 = need2 - common

    # Fulfill remaining type 1 requirements using either type 1 or type 3
    if rem1 > 0:
      total_cost += rem1 * min(costBoth, cost1)

    # Fulfill remaining type 2 requirements using either type 2 or type 3
    if rem2 > 0:
      total_cost += rem2 * min(costBoth, cost2)

    return total_cost