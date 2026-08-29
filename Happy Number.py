class Solution:
    def isHappy(self, n: int) -> bool:
        def sqr(n):
            total= 0
            while n > 0:
                ld= n%10
                total = total+ ld*ld
                n= n//10
            return total
        slow= sqr(n)
        fast= sqr(n)
        while (fast != 1):
            slow=sqr(slow)
            fast=sqr(sqr(fast))
            if slow== fast and slow != 1:
                return False
        return True