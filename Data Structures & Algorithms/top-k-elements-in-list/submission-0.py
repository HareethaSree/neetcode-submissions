class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for i in range (len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i],0)+1

        res = []

        sorted_hash= dict(sorted(hash_map.items(), key=lambda x: x[1], reverse=True))

        for num, count in sorted_hash.items():
            res.append(num)
        
        return res[:k]
        

        