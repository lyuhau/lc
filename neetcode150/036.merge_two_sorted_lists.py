from typing import Optional

from neetcode150.util.list_node import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()
        for i in range(1000):
            if not list1:
                curr.next = list2
                break
            if not list2:
                curr.next = list1
                break
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        return head.next


if __name__ == '__main__':
    solution = Solution()
    print(solution.mergeTwoLists(ListNode.from_list([1, 2, 4]), ListNode.from_list([1, 3, 4])))
