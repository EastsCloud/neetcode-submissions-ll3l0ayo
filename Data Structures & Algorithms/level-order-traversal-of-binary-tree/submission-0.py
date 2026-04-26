# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        cl = [root]
        while(cl):
            res.append(i.val for i in cl)
            nl = []
            for i in cl:
                if i.left:
                    nl.append(i.left)
                if i.right:
                    nl.append(i.right)
            cl = nl
        return res