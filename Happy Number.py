class Solution:
    def isHappy(self, n: int) -> bool:
        def getno(n):
            total=0
            while n > 0:
                ld= n%10
                total= total+ ld **2
                n //= 10
            return total
        slow=n
        fast=getno(n)
        while slow != fast:
            slow=getno(slow)
            fast=getno(getno(fast))
        return slow== 1