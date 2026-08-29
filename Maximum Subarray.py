class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        best= nums[0]
        total=nums[0]
        for i in range(1, n):
            v1= best+ nums[i]
            v2= nums[i]
            best= max(v1, v2)
            total= max(total, best)
        return total