            start2= intervals[i][0]
            end2= intervals[i][1]
            if end1 >= start2:
                start1=start1
                end1= max(end1, end2)
                continue
            else:
                start1= start2
                end1=end2
                res.append([start1, end1])
        for i in range(1, len(intervals)):
        end1= intervals[0][1]
        start1= intervals[0][0]
        res=[]
        intervals.sort()
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
class Solution: