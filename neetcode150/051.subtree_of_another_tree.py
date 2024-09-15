from typing import Optional

from neetcode150.util.tree_node import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue:
            n = queue.pop()
            if not n:
                continue
            if same_tree(n, subRoot):
                return True
            queue.extend((n.left, n.right))
        return False


def same_tree(p, q):
    queue = [(p, q)]
    while queue:
        p, q = queue.pop()
        if p is None and q is None:
            continue
        if (p is None) or (q is None) or p.val != q.val:
            return False
        queue.extend(((p.left, q.left), (p.right, q.right)))
    return True
