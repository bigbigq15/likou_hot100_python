# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        res = ListNode()
        r = res
        v = 0
        while l1 != None and l2 != None:
            val = l1.val + l2.val + v
            if val >= 10:
                v = 1
                val %= 10
            else:
                v = 0
            res.next = ListNode()
            res = res.next
            res.val = val
            l1 = l1.next
            l2 = l2.next
        while l1 != None:
            val = l1.val + v
            if val >= 10:
                v = 1
                val %= 10
            else:
                v = 0
            res.next = ListNode()
            res = res.next
            res.val = val
            l1 = l1.next
        while l2 != None:
            val = l2.val + v
            if val >= 10:
                v = 1
                val %= 10
            else:
                v = 0
            res.next = ListNode()
            res = res.next
            res.val = val
            l2 = l2.next
        if v == 1:
            res.next = ListNode()
            res = res.next
            res.val = 1
        return r.next