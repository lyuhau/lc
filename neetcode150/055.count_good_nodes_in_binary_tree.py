from neetcode150.util.tree_node import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = [(root, root.val)]
        result = 0
        while queue:
            node, max_val = queue.pop()
            if node.val >= max_val:
                result += 1
            max_val = max(max_val, node.val)
            if node.left:
                queue.append((node.left, max_val))
            if node.right:
                queue.append((node.right, max_val))
        return result
