from typing import Optional

from neetcode150.util.tree_node import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return helper(root)[1]


def helper(node):
    if not node:
        return 0, 0
    left_d, left_max = helper(node.left)
    right_d, right_max = helper(node.right)

    return max(left_d, right_d) + 1, max(left_d + right_d, left_max, right_max)
