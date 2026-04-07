# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, greater, less):
            if node is None:
                return True
            if node.val <= greater or node.val >= less:
                return False
            return dfs(node.right, max(greater, node.val), less) and dfs(node.left, greater, min(less, node.val))
        return dfs(root, float('-inf'), float('inf'))