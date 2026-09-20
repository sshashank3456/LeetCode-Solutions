        low= 0
        high= len(nums) -1
        res=-1
        while low <= high:
            guess= (low+high) // 2
            if nums[guess] > target:
                high= guess -1
            elif nums[guess] < target:
                low= guess + 1
            else:
                res= guess
                high= guess-1
        last= res
        return last, first
