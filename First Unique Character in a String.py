class Solution:
    def firstUniqChar(self, s: str) -> int:
        fir= {}
        for i in s:
            if i in fir:
                fir[i]= fir[i]+1
            else:
                fir[i]= 1
        for i in range(len(s)):
            if fir[s[i]] == 1:
                return i
        return -1