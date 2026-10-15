class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        pre = None
        while head != None:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre
