        res=0
        for right in range(n):
            if fruits[right] in freq:
                freq[fruits[right]]+=1
            else:
                freq[fruits[right]]=1
            while len(freq)>2:
                freq[fruits[low]]-=1
            res= max(res, right-low+1)
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1
        return res