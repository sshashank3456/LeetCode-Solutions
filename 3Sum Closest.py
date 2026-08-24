                total= nums[i]+ nums[left]+ nums[right]
                d= abs(target-total)
                if total==target:
                if d<diff:
                    diff=d
                    res_sum=total
                    return res_sum
                if total<target:
                    left+=1
                else:
            while(left<right):
            right=n-1
            left=i+1
        for i in range(n-2):
        res_sum=0
        diff= float('inf')
        n=len(nums)
                    right-=1