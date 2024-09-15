# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, lst):
        if not lst:
            return None
        nodes = [None if val is None else TreeNode(val) for val in lst]
        for i, node in enumerate(nodes):
            if node:
                left_index = 2 * i + 1
                right_index = 2 * i + 2
                if left_index < len(nodes):
                    node.left = nodes[left_index]
                if right_index < len(nodes):
                    node.right = nodes[right_index]
        return nodes[0]

    def __str__(self):
        nodes = []
        queue = [self]
        while any(queue):
            node = queue.pop(0)
            nodes.append(node.val if node else None)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        while nodes and nodes[-1] is None:
            nodes.pop()
        return str(nodes)
