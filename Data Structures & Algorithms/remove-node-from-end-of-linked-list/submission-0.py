class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        l = dummy
        r = head

        for i in range(n):
            r = r.next

        while r:
            r = r.next
            l = l.next

        l.next = l.next.next
        return dummy.next