        curr= t
        prev= None
        time = right - left + 1
        while time:
            nex= curr.next
            curr.next= prev
            prev= curr
            curr= nex
        t.next = curr
            time-=1
            pos+=1
            t= t.next
            before = t
        while pos < left:
        pos= 1
        before= None
        t= head