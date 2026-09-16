        if k == 0:
            return head
        t= head
        count=1 
        while t:
            if count == n-k:
                break
            count+=1
            t=t.next
        last.next= head
        res= t.next
        t.next = None
        return res