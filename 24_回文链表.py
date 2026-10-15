from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         if head.next == None:
#             return True
#         pre = None
#         nxt = head.next
#         head.next = pre
#         pre = head
#         head = nxt
#         while head != None and head.val != pre.val:
#             nxt = head.next
#             head.next = pre
#             pre = head
#             head = nxt
#         if head == None:
#             return False
#         while head != None or pre != None:
#             if (head == None and pre != None) or (head != None and pre == None):
#                 return False
#             if pre.val == head.val:
#                 pre = pre.next
#                 head = head.next
#             else:
#                 return False
#         return True
