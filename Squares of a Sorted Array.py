class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        low=0
        high=len(nums)
        new=[]
        prod=0
        while(low<high):
            prod= abs(nums[low]) ** 2
            new.append(prod)
            low+=1
        new.sort()
        return new
