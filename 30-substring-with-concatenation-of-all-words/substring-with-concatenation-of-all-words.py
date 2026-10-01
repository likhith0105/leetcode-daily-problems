from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        s_len = len(s)
        
        if s_len < total_len:
            return []
        
        word_freq = Counter(words)
        result = []
        
        # Run sliding window for each offset from 0 to word_len - 1
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            count = 0
            
            while right + word_len <= s_len:
                # Get the current word from the right pointer
                w = s[right:right + word_len]
                right += word_len
                
                if w in word_freq:
                    current_count[w] += 1
                    count += 1
                    
                    # If word count exceeds required frequency, slide left pointer
                    while current_count[w] > word_freq[w]:
                        left_w = s[left:left + word_len]
                        current_count[left_w] -= 1
                        count -= 1
                        left += word_len
                    
                    # If all words matched
                    if count == num_words:
                        result.append(left)
                else:
                    # Invalid word found: reset current window
                    current_count.clear()
                    count = 0
                    left = right
                    
        return result