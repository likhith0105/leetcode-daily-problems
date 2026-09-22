class SegmentTree:

  def __init__(self, nums, k):
    self.n = len(nums)
    self.k = k
    self.tree_prod = [1] * (4 * self.n)
    self.tree_pre = [[0] * k for _ in range(4 * self.n)]
    self._build(nums, 0, 0, self.n - 1)

  def _build(self, nums, node, l, r):
    if l == r:
      val = nums[l] % self.k
      self.tree_prod[node] = val
      self.tree_pre[node][val] = 1
      return

    mid = (l + r) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2

    self._build(nums, left_node, l, mid)
    self._build(nums, right_node, mid + 1, r)
    self._merge(node, left_node, right_node)

  def _merge(self, node, left_node, right_node):
    k = self.k
    l_prod = self.tree_prod[left_node]
    r_prod = self.tree_prod[right_node]

    self.tree_prod[node] = (l_prod * r_prod) % k

    # Copy left counts
    pre = list(self.tree_pre[left_node])

    # Extend right counts
    for r_rem, count in enumerate(self.tree_pre[right_node]):
      if count > 0:
        new_rem = (l_prod * r_rem) % k
        pre[new_rem] += count

    self.tree_pre[node] = pre

  def update(self, node, l, r, idx, val):
    if l == r:
      rem = val % self.k
      self.tree_prod[node] = rem
      self.tree_pre[node] = [0] * self.k
      self.tree_pre[node][rem] = 1
      return

    mid = (l + r) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2

    if idx <= mid:
      self.update(left_node, l, mid, idx, val)
    else:
      self.update(right_node, mid + 1, r, idx, val)

    self._merge(node, left_node, right_node)

  def query(self, node, l, r, ql, qr):
    if ql <= l and r <= qr:
      return self.tree_prod[node], self.tree_pre[node]

    mid = (l + r) // 2
    left_node = 2 * node + 1
    right_node = 2 * node + 2

    if qr <= mid:
      return self.query(left_node, l, mid, ql, qr)
    if ql > mid:
      return self.query(right_node, mid + 1, r, ql, qr)

    l_prod, l_pre = self.query(left_node, l, mid, ql, qr)
    r_prod, r_pre = self.query(right_node, mid + 1, r, ql, qr)

    res_prod = (l_prod * r_prod) % self.k
    res_pre = list(l_pre)

    for r_rem, count in enumerate(r_pre):
      if count > 0:
        new_rem = (l_prod * r_rem) % self.k
        res_pre[new_rem] += count

    return res_prod, res_pre


class Solution:

  def resultArray(
      self, nums: List[int], k: int, queries: List[List[int]]
  ) -> List[int]:
    n = len(nums)
    st = SegmentTree(nums, k)
    ans = []

    for idx, val, start, x in queries:
      st.update(0, 0, n - 1, idx, val)
      _, pre_counts = st.query(0, 0, n - 1, start, n - 1)
      ans.append(pre_counts[x])

    return ans