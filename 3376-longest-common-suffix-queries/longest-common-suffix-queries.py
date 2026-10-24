class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        # Helper to decide if index 'i' is better than 'best'
        def update_best(node, i):
            if node.best_index == -1:
                node.best_index = i
            else:
                curr_best = wordsContainer[node.best_index]
                candidate = wordsContainer[i]
                if len(candidate) < len(curr_best):
                    node.best_index = i
                # If lengths are equal, keep the one that appeared earlier (lower index)
                
        # Insert all words (reversed) into the Trie
        for i, word in enumerate(wordsContainer):
            rev_word = word[::-1]
            curr = root
            # Update root with the overall best (shortest, then earliest)
            update_best(curr, i)
            
            for char in rev_word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                update_best(curr, i)
                
        # Process each query
        ans = []
        for q in wordsQuery:
            rev_q = q[::-1]
            curr = root
            last_valid_index = root.best_index
            
            for char in rev_q:
                if char in curr.children:
                    curr = curr.children[char]
                    last_valid_index = curr.best_index
                else:
                    break
            ans.append(last_valid_index)
            
        return ans