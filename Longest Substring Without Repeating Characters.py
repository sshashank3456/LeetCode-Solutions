        res=0
        for high in range(n):
            if s[high] in freq:
                freq[s[high]]+=1
            else:
                freq[s[high]]=1
            while(len(freq)<high-low+1):
                freq[s[low]]-=1
                if freq[s[low]]== 0:
                    del freq[s[low]]
                low+=1
            res=max(res, high-low+1)
        freq={}
        low=0
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
class Solution: