from typing import Optional

from neetcode150.util.tree_node import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = [root]
        while stack:
            while stack[-1]:
                stack.append(stack[-1].left)
            stack.pop()
            if stack:
                node = stack.pop()
                n += 1
                if n == k:
                    return node.val
                stack.append(node.right)
