        while low <= high:
            guess= (low+high) // 2
            hour=0
            for i in range(n):
                hour= hour + piles[i] // guess
                if piles[i] % guess != 0:
                    hour+=1
            if hour > h:
                low= guess+1
            else:
                res= guess
        res= -1
        high= max(piles)
        low= 1
        n= len(piles)
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
class Solution: