    def isHappy(self, n: int) -> bool:
        def fun(n):
            total = 0
            while n > 0:
                ld= n%10
                total= total + ld**2
                n=n//10
            return total
        slow= fun(n)
        fast= fun(n)
        while fast != 1:
            slow= fun(slow)
            fast= fun(fun(fast))
            if slow == fast and slow != 1:
                return False
        return True