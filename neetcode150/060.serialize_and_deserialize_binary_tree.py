from typing import Optional, List

from neetcode150.util.tree_node import TreeNode


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preorder_ser = []
        def preorder(node):
            if not node:
                return
            preorder_ser.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)

        inorder_ser = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_ser.append(str(node.val))
            inorder(node.right)
        inorder(root)

        return " ".join(preorder_ser) + '|' + " ".join(inorder_ser)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preorder_ser, inorder_ser = data.split('|')
        preorder = list(map(int, preorder_ser.split()))
        inorder = list(map(int, inorder_ser.split()))
        return self._buildTree(preorder, inorder)

    def _buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
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
    s = Codec()

    root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    serialize = s.serialize(root)
    deserialize = s.deserialize(serialize)
    print(root, serialize, deserialize)

    root = None
    serialize = s.serialize(root)
    deserialize = s.deserialize(serialize)
    print(root, serialize, deserialize)
