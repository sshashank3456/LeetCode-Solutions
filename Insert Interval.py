            res.append(intervals[i])
        start1= res[0][0]
        end1= res[0][1]
        rev=[]
        for i in range(len(res)):
            start2= res[i][0]
            end2= res[i][1]
            if end1 >= start2:
                insert =True
                res.append(newInterval)
                start1= start1
                end1= max(end1, end2)
            if insert == False and intervals[i][0] >= newInterval[0]:
        for i in range(n):
        insert= False
        if insert == False:
            res.append(newInterval)
        res=[]
        n= len(intervals)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]: