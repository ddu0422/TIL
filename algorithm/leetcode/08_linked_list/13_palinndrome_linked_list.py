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

    def isPalindrome2(self, head: ListNode) -> bool:
        # solve 2
        # slow의 위치부터 거꾸로 이동
        reverse = None
        # slow runner, fast runner를 이용
        slow = fast = head

        # 보통 fast runner는 2칸, slow runner는 1칸 이동
        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next

        if fast:
            slow = slow.next

        while reverse and reverse.val == slow.val:
            slow, reverse = slow.next, reverse.next

        # reverse가 끝까지 가야(None 상태) 팰린드롬을 만족
        return not reverse
