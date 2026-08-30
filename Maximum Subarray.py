class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxsub=nums[0]
        res= nums[0]
        for i in range(1, n):
            maxsub= max(maxsub + nums[i], nums[i])
            res= max(res, maxsub)
        return res