from typing import Optional

from neetcode150.util.list_node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nth = head
        for i in range(n+1):
            if not nth:
                return head.next
            nth = nth.next
        curr = head
        while nth:
            curr = curr.next
            nth = nth.next
        curr.next = curr.next.next
        return head


if __name__ == '__main__':
    solution = Solution()
    head = ListNode.from_list([1, 2, 3, 4, 5])
    head = solution.removeNthFromEnd(head, 2)
    print(head)
    head = ListNode.from_list([1, 2, 3, 4, 5])
    head = solution.removeNthFromEnd(head, 5)
    print(head)
