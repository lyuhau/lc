from typing import Optional

from neetcode150.util.tree_node import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        stack = [root]
        while stack:
            while stack[-1]:
                stack.append(stack[-1].left)
            stack.pop()
            if stack:
                node = stack.pop()
                if node.val <= prev:
                    return False
                prev = node.val
                stack.append(node.right)
        return True
