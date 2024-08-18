# Definition for singly-linked list.
# 주어진 2개의 링크드 리스트에 있는 수를 더 해서 다시 링크드 리스트로 반환하는 문제이다.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = dummy = ListNode(-1)  # 간결한 로직 구현을 위해 더미노드를 사용하는 것은 LinkedList 를 풀 때 효율적
        carry = 0
        while l1 and l2:
            carry, digit = divmod(l1.val + l2.val + carry, 10)  # 몫(carry)과 나머지(digit)
            node.next = ListNode(digit)
            l1, l2, node = l1.next, l2.next, node.next
        l = l1 or l2
        while l:
            carry, digit = divmod(l.val + carry, 10)
            node.next = ListNode(digit)
            l, node = l.next, node.next
        if carry:
            node.next = ListNode(carry)
        return dummy.next
