        for high in range(n):
            f[ord(s[high])]+=1
            maxcnt= max(f)
            length= high-low+1
            diff=length- maxcnt
            while(diff>k):
                f[ord(s[low])]-=1
                low+=1
                maxcnt= max(f)
                length= high-low+1
                diff=length- maxcnt
            res= max(res, high-low+1)
        return res