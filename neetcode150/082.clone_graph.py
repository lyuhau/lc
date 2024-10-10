# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        start = node.val

        # clone nodes
        new_nodes = {}
        queue = [node]
        while queue:
            node = queue.pop()
            if node.val in new_nodes:
                continue
            new_nodes[node.val] = Node(node.val)
            for neighbor in node.neighbors:
                new_nodes[node.val].neighbors.append(neighbor.val)
                queue.append(neighbor)

        # convert neighbors to nodes
        for val, node in new_nodes.items():
            node.neighbors = [new_nodes[neighbor] for neighbor in node.neighbors]

        return new_nodes[start]
