        total=0
        for num in nums:
            total= total+num
        for i in range(1, n):
            prevminsum= minsum
            prevmaxsum= maxsum
            minsum= min(prevminsum + nums[i], nums[i])
            maxsum= max(prevmaxsum + nums[i], nums[i])
        if max_total < 0:
            min_total = min(min_total, minsum)
            max_total = max(max_total, maxsum)
            return max_total
        res= total - min_total
        return max(res, max_total)
        