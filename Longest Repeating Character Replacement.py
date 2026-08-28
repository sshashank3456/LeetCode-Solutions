    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        low=0
        res=0
        freq={}
        for high in range(n):
            if s[high] in freq:
                freq[s[high]]+=1
            else:
                freq[s[high]]=1
        maxcnt=0
            maxcnt= max(freq.values())
            while((high-low+1) - maxcnt > k):
                freq[s[low]]-=1
                low+=1
            res= max(res, high-low+1)
        return res