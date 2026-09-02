        for i in range(len(nums)):
            total= total + nums[i]
            rem= total% k
            if rem < 0:
                rem+= k
            if rem in freq:
        res=0
                res= res+ freq[rem]
            if rem in freq:
                freq[rem]+=1
            else:
                freq[rem]=1
        return res