from typing import Optional

from neetcode150.util.tree_node import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [(p, q)]
        while queue:
            p, q = queue.pop()
            if p is None and q is None:
                continue
            if (p is None) or (q is None) or p.val != q.val:
                return False
            queue.extend(((p.left, q.left), (p.right, q.right)))
        return True
