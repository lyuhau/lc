from typing import Optional

from neetcode150.util.tree_node import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        m = 0
        queue = [(root, 1)]
        while queue:
            n, d = queue.pop()
            if not n:
                continue
            queue.extend(((n.left, d + 1), (n.right, d + 1)))
            m = max(m, d)
        return m
