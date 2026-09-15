class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        have={}
        for i in range(len(text)):
            if text[i] in have:
                have[text[i]] +=1
            else:
                have[text[i]] = 1
        need= {'b': 1, 'a' : 1, 'l' : 2, 'o' : 2, 'n' : 1}
        res= float('inf')
            time= have.get(key, 0) // need[key]
            res= min(res, time)
        for key in need:
        return res