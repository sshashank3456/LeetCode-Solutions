        low= 0
        high= len(nums) - 1
        first= res
                high =  guess - 1
                res= guess
            else:
                low = guess + 1
            elif nums[guess] < target:
                high = guess- 1
        res= -1
            if nums[guess] > target:
            guess = (low + high) // 2
        while low <= high :
        res= -1
        high= len(nums) - 1
        low= 0
    def searchRange(self, nums: list[int], target: int) -> list[int]:
class Solution: