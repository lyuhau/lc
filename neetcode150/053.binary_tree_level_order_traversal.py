from itertools import groupby
from typing import Optional, List

from neetcode150.util.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, 1)]
        i = 0
        while i < len(queue):
            n, d = queue[i]
            i += 1
            if n.left:
                queue.append((n.left, d + 1))
            if n.right:
                queue.append((n.right, d + 1))
        answer = [
            [n.val for n, d in group]
            for _, group in groupby(queue, key=lambda x: x[1])
        ]
        return answer


if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode.from_list([1, 2, 3, 4, 5, 6, 7])
    actual = solution.levelOrder(tree)
    print(actual)
    assert actual == [[1], [2, 3], [4, 5, 6, 7]]
