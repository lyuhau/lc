from typing import Optional

from neetcode150.util.list_node import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        end = head
        half = head
        while end and end.next:
            half = half.next
            end = end.next.next

        left = head
        right = reverseList(half)
        while right.next:
            left_next = left.next
            right_next = right.next
            left.next = right
            right.next = left_next
            left = left_next
            right = right_next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
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


if __name__ == '__main__':
    solution = Solution()
    head = ListNode.from_list([1, 2, 3, 4])
    solution.reorderList(head)
    print(head)
    head = ListNode.from_list([1, 2, 3, 4, 5])
    solution.reorderList(head)
    print(head)
    head = ListNode.from_list([0, 1, 2, 3, 4, 5, 6])
    solution.reorderList(head)
    print(head)
