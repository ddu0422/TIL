from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # solve 1
        if not head:
            return True

        queue = deque()
        node = head

        while node:
            queue.append(node.val)
            node = node.next

        while len(queue) > 1:
            if queue.popleft() != queue.pop():
                return False

        return True
