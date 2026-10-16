# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        res = ListNode(0,head)
        pre = res
        while pre.next != None and pre.next.next != None:
            left = pre.next
            right = left.next
            left.next = right.next
            right.next = left
            pre.next = right
            pre = left
        return res.next