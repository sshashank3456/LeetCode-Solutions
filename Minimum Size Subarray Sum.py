class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        low=0
        sum=0
        res= float('inf')
        for high in range(n):
            sum= sum + nums[high]
            while sum >= target:
                sum= sum - nums[low]
                low+=1
        if res== float('inf'):
            return 0
                res= min(res, high-low +1)
        return res