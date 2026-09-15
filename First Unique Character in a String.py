class Solution:
    def firstUniqChar(self, s: str) -> int:
        n= len(s)
        res= {}
        for i in range(n):
            if s[i] in res:
                res[s[i]]+=1
            else:
                res[s[i]] = 1
        for i in range(n):
            if res[s[i]] == 1:
                return i
        return -1