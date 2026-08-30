    def maxAbsoluteSum(self, nums: List
    [int]) -> int:
        minsum=nums[0]
        maxsum= nums[0]
        res=abs(nums[0])
        for i in range(1, len(nums)):
            prevminsum= minsum
            prevmaxsum= maxsum
            minsum= minsum + nums[i]
            maxsum= maxsum+ nums[i]
            v1= min(minsum, nums[i])
            v2= max(maxsum, nums[i])
            res= max(res, abs(v1), abs(v2))
        return res
            minsum= v1
            maxsum= v2
