import heapq
from typing import List, Optional

from neetcode150.util.list_node import ListNode


class HeapNode:
    def __init__(self, val, key=lambda x: x):
        self.val = val
        self.key = key

    def __lt__(self, other):
        return self.key(self.val) < self.key(other.val)


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        key = lambda x: x.val
        heap = [HeapNode(node, key) for node in lists if node]
        heapq.heapify(heap)
        head = curr = ListNode()
        while heap:
            node = heapq.heappop(heap).val
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, HeapNode(node.next, key))
        return head.next


if __name__ == '__main__':
    solution = Solution()

    # Example 1
    lists = [
        ListNode.from_list([1, 4, 5]),
        ListNode.from_list([1, 3, 4]),
        ListNode.from_list([2, 6]),
    ]
    expected = ListNode.from_list([1, 1, 2, 3, 4, 4, 5, 6])
    assert (result := solution.mergeKLists(lists)) == expected, f"{result}"

    # Example 2
    lists = []
    expected = None
    assert (result := solution.mergeKLists(lists)) == expected, f"{result}"

    # Example 3
    lists = [None]
    expected = None
    assert (result := solution.mergeKLists(lists)) == expected, f"{result}"

    print("PASSED")
