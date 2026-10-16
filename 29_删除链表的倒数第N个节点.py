# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count = [n,0]
        def rnf(head,count):
            if head == None:
                return None
            rnf(head.next, count)
            count[0] -=1
            count[1] +=1
            if count[0] == -1:
                r1 = head.next
                head.next = head.next.next
                r1.next = None
            return head
        rnf(head,count)
        if count[1] == n:
            return head.next
        return head

class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # 用列表保存 n，让所有递归层共享
        count = [n]

        def dfs(node):
            if node is None:
                return None
            node.next = dfs(node.next)   # 先递归到末尾
            count[0] -= 1                # 归的过程中从后往前数
            if count[0] == 0:
                return node.next         # 删除当前节点
            return node

        return dfs(head)