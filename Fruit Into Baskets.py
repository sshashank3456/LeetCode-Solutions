    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        low=0
        res=0
        freq={}
        for high in range(n):
            if fruits[high] in freq:
                freq[fruits[high]]+=1
            else:
                freq[fruits[high]]= 1
            while(len(freq)>2):
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1
            res= max(res, high-low+1)
        return res
