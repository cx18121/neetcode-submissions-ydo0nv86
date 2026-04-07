# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        vals = []
        q = deque([root])
        nq = []
        while q: 
            n = q.popleft()
            vals.append(n.val)
            if n.left:
                nq.append(n.left)
            if n.right:
                nq.append(n.right)
            if len(q) == 0:
                q = deque(nq[:])
                res.append(vals)
                vals = []
                nq = []
                           
        return res;