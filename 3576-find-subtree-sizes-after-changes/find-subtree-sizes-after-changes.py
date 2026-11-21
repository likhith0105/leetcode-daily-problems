from collections import defaultdict


class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        children = defaultdict(list)
        for node in range(1, n):
            children[parent[node]].append(node)

        # new_parent[x] = closest ancestor y of x with s[y] == s[x], or -1 if none
        new_parent = [-1] * n
        # last_seen[c] = stack of ancestor nodes having character c
        last_seen: dict[str, list[int]] = defaultdict(list)

        def dfs_find_new_parents(node: int) -> None:
            ch = s[node]
            if last_seen[ch]:
                new_parent[node] = last_seen[ch][-1]

            last_seen[ch].append(node)
            for nxt in children[node]:
                dfs_find_new_parents(nxt)
            last_seen[ch].pop()

        dfs_find_new_parents(0)

        # Build the final tree after simultaneous edge reassignments
        final_children = defaultdict(list)
        for node in range(1, n):
            p = new_parent[node] if new_parent[node] != -1 else parent[node]
            final_children[p].append(node)

        ans = [1] * n

        def dfs_subtree_size(node: int) -> int:
            total = 1
            for nxt in final_children[node]:
                total += dfs_subtree_size(nxt)
            ans[node] = total
            return total

        dfs_subtree_size(0)
        return ans