class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n= len(nums)
        left=0
        for i in range(n):
            total = total + nums[i]
        for i in range(n):
            right= total-left- nums[i]
            if left == right:
                return i
        total=0
            left= left + nums[i]
        return -1