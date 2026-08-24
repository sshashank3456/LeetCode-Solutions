                sum2= nums[left]+nums[right]
                if sum2==sum1:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
            while(left<right):
            sum1= -1 * nums[i]
            right=len(nums)-1
            left= i+1
        for i in range(0, len(nums)-2):
        res=[]
        nums.sort()
    def threeSum(self, nums: list[int]) -> list[list[int]]:
class Solution:
            if i>0 and nums[i]== nums[i-1]:
                continue