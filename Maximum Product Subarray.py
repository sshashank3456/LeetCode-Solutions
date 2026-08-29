class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxbest=nums[0]
        minbest=nums[0]
        res=nums[0]
        for i in range(1, n):
            v1= maxbest * nums[i]
            v2= minbest * nums[i]
            v3= nums[i]
            maxbest= max(v3, max(v2, v1))
            minbest= min(v3, min(v1, v2))
            res= max(res, max(minbest, maxbest))
        return res