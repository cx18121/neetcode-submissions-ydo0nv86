# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def con(node, l): 
            if node is None:
                return None
            if node.val == l.val:
                return True
            return con(node.left, l) or con(node.right, l)

        if root is None:
            return None
        if con(root, p) and con(root, q):
            a = self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)
            if not a:
                return root
            else:
                return a
        else:
            return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)