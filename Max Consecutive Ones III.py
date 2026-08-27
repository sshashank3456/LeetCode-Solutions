            if nums[high] in freq:
                freq[nums[high]]+=1
            else:
                freq[nums[high]]= 1
            maxcnt= max(freq.values())
            while(high-low+1 - maxcnt > k):
                freq[nums[low]]-=1
                if freq[nums[low]]==0:
        for high in range(n):
        maxcnt=0
        freq={}
        res=0
        low=0
        n=len(nums)
    def longestOnes(self, nums: List[int], k: int) -> int:
class Solution:
        if k==0:
            return 0