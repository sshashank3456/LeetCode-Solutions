class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxprod= nums[0]
        minprod= nums[0]
        res= nums[0]
        for i in range(1, n):
            v1= maxprod * nums[i]
            v2= minprod * nums[i]
            v3= nums[i]
            res= max(res, maxprod)
            maxprod= max(v1, v2, v3)
            minprod= min(v1, v2, v3)
        return res