class Solution:
    def minOperations(self, s: str) -> int:
        if s == "".join(sorted(s)):
            return 0
        if len(s) == 2:
            return -1
        
        mn = min(s)
        mx = max(s)
        
        # Check if the minimum character is at the start (not whole string) 
        # or the maximum character is at the end (not whole string)
        if (s[0] == mn and s != mn * len(s)) or (s[-1] == mx and s != mx * len(s)):
            return 1
            
        # Check if no minimum exists in any proper prefix and no maximum exists in any proper suffix
        # Effectively: can we sort with 2 operations?
        # If the string can be sorted, check if 2 operations are enough, otherwise 3.
        # Actually, if mn is anywhere except index 0 (and can be brought to front) 
        # or mx is anywhere except index len(s)-1...
        
        has_mn_in_prefix = any(c == mn for c in s[:-1])
        has_mx_in_suffix = any(c == mx for c in s[1:])
        
        if not has_mn_in_prefix and not has_mx_in_suffix:
            return 3
            
        return 2