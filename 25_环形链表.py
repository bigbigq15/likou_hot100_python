from typing import Optional
from collections import defaultdict

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        while head != None and head.next != None:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast != None:
            slow = head.next
            fast = head.next.next
            if slow == fast:
                return True
        return False
