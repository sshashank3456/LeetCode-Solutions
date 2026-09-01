class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total= 0
        freq= {0: 1}
        for i in range(len(nums)):
            total= total+nums[i]
            ques= total-k
            if ques in freq:
        res=0
                res= res+ freq[ques]
            if total in freq:
                freq[total]+=1
            else:
                freq[total] = 1
        return res 
