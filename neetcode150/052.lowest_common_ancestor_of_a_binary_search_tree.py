from neetcode150.util.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        m = {root.val: root}
        parents = {root.val: None}
        queue = [root]
        found_p = False
        found_q = False
        while queue:
            n = queue.pop()
            if not n:
                continue
            m[n.val] = n
            queue.extend((n.left, n.right))
            if n.left:
                parents[n.left.val] = n.val
            if n.right:
                parents[n.right.val] = n.val
            if n == p:
                found_p = True
            if n == q:
                found_q = True
            if found_p and found_q:
                break
        p_parents = []
        n = p.val
        while n is not None:
            p_parents.append(n)
            n = parents[n]
        q_parents = []
        n = q.val
        while n is not None:
            q_parents.append(n)
            n = parents[n]
        last_same = None
        for p, q in zip(reversed(p_parents), reversed(q_parents)):
            if p == q:
                last_same = p
            else:
                break
        return m[last_same]


if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode.from_list([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = tree.left
    q = tree.right
    actual = solution.lowestCommonAncestor(tree, p, q)
    print(actual)
    assert actual == tree.val

    tree = TreeNode.from_list([5,3,8,1,4,7,9,None,2])
    p = tree.left
    q = tree.right
    actual = solution.lowestCommonAncestor(tree, p, q)
    print(actual)
    assert actual == tree.val
