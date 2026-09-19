                    if nums[0] > target:
                        low= guess + 1
                    else:
                        high= guess - 1
            else:
                if nums[guess] > target:
                    high= guess - 1
                else:
                    if nums[n-1] < target:
                        high= guess -1
                    else:
                        low= guess + 1
        return -1