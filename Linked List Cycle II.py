#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow= head
        fast=head
        while fast is not None and fast.next is not None:
            slow= slow.next
            fast= fast.next.next
                    slow= slow.next
                    fast= fast.next
            if slow== fast:
                return slow
                while slow != fast:
                slow= head
        return None
