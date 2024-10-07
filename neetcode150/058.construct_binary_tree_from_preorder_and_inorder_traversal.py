from typing import List, Optional

from neetcode150.util.tree_node import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        order = {val: i for i, val in enumerate(inorder)}
        root = TreeNode(preorder[0])
        path = [root]
        for val in preorder[1:]:
            node = TreeNode(val)
            if order[val] < order[path[-1].val]:
                path[-1].left = node
            else:
                while path and order[val] > order[path[-1].val]:
                    last = path.pop()
                last.right = node
            path.append(node)
        return root


if __name__ == '__main__':
    s = Solution()
    print(s.buildTree([1,2,3,4], [2,1,3,4]))
    print(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
    print(s.buildTree([-1], [-1]))
    print(s.buildTree([1, 2, 3], [1, 2, 3]))
    print(s.buildTree([1, 2, 3], [1, 3, 2]))
    print(s.buildTree([1, 2, 3], [2, 1, 3]))
    print(s.buildTree([1, 2, 3], [2, 3, 1]))
    print(s.buildTree([1, 2, 3], [3, 1, 2]))
    print(s.buildTree([1, 2, 3], [3, 2, 1]))
