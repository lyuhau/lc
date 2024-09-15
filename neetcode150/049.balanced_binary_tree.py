from typing import Optional

from neetcode150.util.tree_node import TreeNode


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return helper(root)[1]


def helper(node):
    if not node:
        return 0, True

    left_d, left_b = helper(node.left)
    right_d, right_b = helper(node.right)

    return max(left_d, right_d) + 1, left_b and right_b and abs(left_d - right_d) <= 1
