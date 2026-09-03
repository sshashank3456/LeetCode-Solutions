                if end1 >= start2:
                    s= max(start1, start2)
                    e= min(end1, end2)
                    res.append([s, e])
            if start1 <= start2:
            else:
                if end2 >= start1:
                    s= max(start1, start2)
                    e= min(end1, end2)
                    res.append([s, e])
            if end1 <= end2:
                i+=1
            else:
                j+=1
        return res