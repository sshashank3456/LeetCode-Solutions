    def longestPalindrome(self, s: str) -> int:
        have={}
        for i in range(len(s)):
            if s[i] in have:
                have[s[i]] += 1
            else:
                have[s[i]] = 1
        odd= False
        res= 0
        for key in have:
            if have[key] % 2 == 0:
                res= res + have[key]
            else:
                odd= True
        if odd == False:
            return res
        else: