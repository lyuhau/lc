from typing import Optional

from neetcode150.util.list_node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass


if __name__ == '__main__':
    solution = Solution()
    head = ListNode.from_list([1, 2, 3, 4, 5])
    head = solution.removeNthFromEnd(head, 2)
    print(head)
