class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_group = defaultdict(list)

        for word in strs:
            count = [0]*26
            
            for ch in word:
                count[ord(ch)-ord('a')]+=1
            hash_group[tuple(count)].append(word)
        return list(hash_group.values())

            
        