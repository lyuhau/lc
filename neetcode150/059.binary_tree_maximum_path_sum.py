from typing import Optional

from neetcode150.util.tree_node import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def downward(node):
            if not node:
                return
            downward(node.left)
            downward(node.right)
            node.downward = max(
                node.val,
                node.val + node.left.downward if node.left else float('-inf'),
                node.val + node.right.downward if node.right else float('-inf'),
            )
        downward(root)

        result = float('-inf')
        def upward(node):
            if not node:
                return
            nonlocal result
            result = max(
                result,
                node.val,
                node.val + node.left.downward if node.left else float('-inf'),
                node.val + node.right.downward if node.right else float('-inf'),
                node.val + node.left.downward + node.right.downward if node.left and node.right else float('-inf'),
            )
            upward(node.left)
            upward(node.right)
        upward(root)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))))
    print(s.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
    print(s.maxPathSum(TreeNode(-3)))
    print(s.maxPathSum(TreeNode(-3, TreeNode(-1))))
