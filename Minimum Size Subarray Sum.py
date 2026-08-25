class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low=0
        high=0
        sumof=0
        n=len(nums)
        while(high<n):
            while(sumof>=target):
                length=high-low+1
        res=float('inf')
                res= min(res, length)
                sumof=sumof-nums[low]
                low+=1
            high+=1
            sumof=sumof+ nums[high]
        if res == float('inf'):
            return 0
        return res