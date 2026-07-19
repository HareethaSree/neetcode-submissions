class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 1
        max_length = 1
        n = len(nums)
        nums = sorted(nums)
        print(nums)

        if not nums:
            return 0

        for i in range(1,n):
            if nums[i] == nums[i-1]+1:
                length +=1
                print(length)
            elif nums[i] == nums[i-1]:
                length = length
                print(length)
            else:
                max_length = max(length, max_length)
                length = 1
            max_length = max(length, max_length)
        return max_length
                

        