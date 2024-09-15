from typing import Optional

from neetcode150.util.list_node import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = scout = head
        while True:
            curr = curr.next
            scout = scout.next
            if not scout:
                return False
            scout = scout.next
            if not scout:
                return False
            if curr == scout:
                return True
