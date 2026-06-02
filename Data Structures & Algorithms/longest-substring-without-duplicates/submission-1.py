class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        left = 0 
        length_substring = 0 

        for r in range(len(s)):
            if s[r] in hash_map:
                left = max(hash_map[s[r]]+1,left)
            hash_map[s[r]]=r
            length_substring = max(length_substring, r-left+1)
        return length_substring
        

        
        