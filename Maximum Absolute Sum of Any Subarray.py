class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minsum=nums[0]
        maxsum=nums[0]
        res=abs(nums[0])
        for i in range(1, len(nums)):
            maxsum= max(maxsum+ nums[i], nums[i])
            res= max(res, abs(maxsum), abs(minsum))
        return res
            minsum= min(minsum+ nums[i], nums[i])
            