        high=n-1
        while(mid<=high):
            if nums[mid] == 0:
                nums[mid], nums[low]= nums[low], nums[mid]
                low+=1
                mid+=1
            elif nums[mid]== 1:
                mid+=1
            else:
                nums[mid], nums[high]= nums[high], nums[mid]
        mid=0
        low=0
        n=len(nums)
    def sortColors(self, nums: List[int]) -> None:
        return
class Solution:
                high-=1
        