            diff= zero-one
            if diff==0:
                res= max(res, i+1)
                continue
            if diff not in freq:
                freq[diff] = i
            else:
                idx= freq[diff]
                length= i - idx
                res= max(res, length)
                one+=1
            else:
                zero+=1
            if nums[i]==0:
        for i in range(n):
        res= 0
        return res
