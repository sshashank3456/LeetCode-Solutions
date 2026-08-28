class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        low=0
        zero=0
        for high in range(n):
            if nums[high]==0:
                zero+=1
            while( zero> k):
                if nums[low]==0:
                    zero-=1
                low+=1
        res=0
            res= max(res, high-low+1)
        return res