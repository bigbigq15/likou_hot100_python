from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        r = res
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
                res = res.next
            else:
                res.next = list2
                list2 = list2.next
                res = res.next
        if list1 == None:
            res.next = list2
        elif list2 == None:
            res.next = list1
        return r.next
