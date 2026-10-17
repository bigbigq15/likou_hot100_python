class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        n = 1
        h = head
        p = ListNode(0, head)
        res = []
        while head != None:
            head = head.next
            if n == k:
                pre = head
                r = h
                while h != head:
                    nxt = h.next
                    h.next = pre
                    pre = h
                    h = nxt
                n = 0
                p.next = pre
                if not res:
                    res.append(pre)
                p = r
            n += 1
        return res[0] if res else p.next
