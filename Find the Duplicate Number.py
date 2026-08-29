class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n= len(nums)
        freq= {}
        for num in nums:
            if num in freq:
                return num
            freq[num] = 1