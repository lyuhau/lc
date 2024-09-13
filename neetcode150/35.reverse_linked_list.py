from typing import Optional

from neetcode150.util.list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next is None:
            return head

        curr = head
        next_ = head.next
        head.next = None
        while next_:
            next_next = next_.next
            next_.next = curr
            curr = next_
            next_ = next_next

        return curr
