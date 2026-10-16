# Definition for singly-linked list.
from typing import Optional


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




class Solution:
    # l1 和 l2 为当前遍历的节点，carry 为进位
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None and carry == 0:  # 递归边界
            return None

        s = carry
        if l1:
            s += l1.val  # 累加进位与节点值
            l1 = l1.next
        if l2:
            s += l2.val
            l2 = l2.next

        # s 除以 10 的余数为当前节点值，商为进位
        return ListNode(s % 10, self.addTwoNumbers(l1, l2, s // 10))