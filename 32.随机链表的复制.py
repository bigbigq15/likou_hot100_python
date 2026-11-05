class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.cachedNode = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        if head not in self.cachedNode:
            headNew = Node(head.val)
            self.cachedNode[head] = headNew
            headNew.next = self.copyRandomList(head.next)
            headNew.random = self.copyRandomList(head.random)
        return self.cachedNode[head]