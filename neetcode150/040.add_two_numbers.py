from typing import Optional

from neetcode150.util.list_node import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = result = ListNode()
        carry = 0
        while l1 or l2 or carry:
            l1, n1 = (None, 0) if not l1 else (l1.next, l1.val)
            l2, n2 = (None, 0) if not l2 else (l2.next, l2.val)
            carry, digit = divmod(n1 + n2 + carry, 10)
            curr.next = ListNode(digit)
            curr = curr.next

        return result.next
