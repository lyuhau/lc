from typing import Optional, List

from neetcode150.util.tree_node import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        result = []
        while queue:
            result.append(queue[-1].val)
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.rightSideView(TreeNode.from_list([1, 2, 3, 4, 5, 6, 7])))
    print(s.rightSideView(TreeNode.from_list([1, 2, 3, None, 5, None, 4])))
    print(s.rightSideView(TreeNode.from_list([1, None, 3])))
    print(s.rightSideView(TreeNode.from_list([1, 2, 3, 4])))
    print(s.rightSideView(None))
