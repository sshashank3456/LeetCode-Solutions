                res= min(res, high-low+1)
                sumof= sumof- nums[low]
                low+=1
        if res== float('inf'):
        n= len(nums)
        low=0
        res=float('inf')
        sumof=0
        for high in range(n):
            sumof= sumof + nums[high]
            while( sumof >= target):
            return 0
        return res
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
class Solution: