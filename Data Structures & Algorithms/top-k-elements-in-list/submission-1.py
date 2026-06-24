class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hash = {}
        frequency_bucket = [[] for i in range(len(nums)+1)]

        for num in nums:
            count_hash[num] = count_hash.get(num, 0)+1
        
        for num, frequency in count_hash.items():
            frequency_bucket[frequency].append(num)
        
        res = []

        for i in range (len(frequency_bucket)-1, 0, -1):
            for num in frequency_bucket[i]:
                res.append(num)
                if len(res)== k:
                    return res


        