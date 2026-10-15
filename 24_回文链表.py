from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     if head.next == None:
    #         return True
    #     pre = None
    #     nxt = head.next
    #     head.next = pre
    #     pre = head
    #     head = nxt
    #     while head != None and head.val != pre.val:
    #         nxt = head.next
    #         head.next = pre
    #         pre = head
    #         head = nxt
    #     if head == None:
    #         return False
    #     while head != None or pre != None:
    #         if (head == None and pre != None) or (head != None and pre == None):
    #             return False
    #         if pre.val == head.val:
    #             pre = pre.next
    #             head = head.next
    #         else:
    #             return False
    #     return True
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head

        def is_pal(right: Optional[ListNode]) -> bool:
            # 「递」，先把 right 移到链表末尾
            if right.next and not is_pal(right.next):
                return False
            # 「归」的过程就是在从右到左遍历链表
            nonlocal left
            if left.val != right.val:
                return False
            left = left.next  # left 往右走
            return True  # 归，right 会往左走

        return is_pal(head)

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head

        def is_pal(right: None | ListNode):
            if right.next and not is_pal(right.next):
                return False
            nonlocal left
            if left.val == right.val:
                left = left.next
                return True
            else:
                return False

        return is_pal(head)