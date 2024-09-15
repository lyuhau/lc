from typing import Optional

from neetcode150.util.list_node import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_group(head):
            prev = None
            curr = head
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev, curr

        group_head = group_prev = ListNode()
        group_head.next = head
        while True:
            scout = group_prev.next
            for _ in range(k):
                if not scout:
                    return group_head.next
                scout = scout.next

            prev, curr = reverse_group(group_prev.next)
            group_prev.next.next = curr
            tmp = group_prev.next
            group_prev.next = prev
            group_prev = tmp


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseKGroup(ListNode.from_list([]), 2))
    print(solution.reverseKGroup(ListNode.from_list([1]), 2))
    print(solution.reverseKGroup(ListNode.from_list([1, 2]), 2))
    print(solution.reverseKGroup(ListNode.from_list([1, 2, 3, 4, 5]), 2))
    print(solution.reverseKGroup(ListNode.from_list([1, 2, 3, 4, 5, 6]), 2))
    print(solution.reverseKGroup(ListNode.from_list([1, 2, 3, 4, 5, 6]), 6))
    print(solution.reverseKGroup(ListNode.from_list([1, 2, 3, 4, 5, 6]), 7))
