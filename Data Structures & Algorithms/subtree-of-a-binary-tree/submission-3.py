# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(t1, t2):
            if t1 is None:
                return t2 is None
            if t2 is None:
                return t1 is None
            if t1.val != t2.val:
                return False
            return equal(t1.left, t2.left) and equal (t1.right, t2.right)
        
        if root is None:
            return False
        return equal(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
