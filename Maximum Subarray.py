class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxsub=nums[0]
        res= nums[0]
        for i in range(1, n):
            v1= maxsub + nums[i]
            v2= nums[i]
            res= max(res, maxsub)
            maxsub= max(v1, v2)
        return res