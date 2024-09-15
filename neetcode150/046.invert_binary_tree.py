from typing import Optional

from neetcode150.util.tree_node import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        while queue:
            n = queue.pop()
            if not n:
                continue
            queue.extend((n.left, n.right))
            n.left, n.right = n.right, n.left
        return root
