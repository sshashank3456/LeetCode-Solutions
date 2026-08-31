class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n= len(nums)
        minsum=nums[0]
        maxsum=nums[0]
        res=abs(nums[0])
        for i in range(1, n):
            prevminsum= minsum
            prevmaxsum= maxsum
            minsum= min(prevminsum + nums[i], nums[i])
            maxsum= max(prevmaxsum+ nums[i], nums[i])
            res= max(res, max(abs(minsum), abs(maxsum)))
        return res