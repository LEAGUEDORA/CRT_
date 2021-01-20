# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        if root.left is None:
            l =  []
        else:
            l = self.inorderTraversal(root.left)
        
        if root.right is None:
            r =  []
        else:
            r = self.inorderTraversal(root.right)
        
        return l  + [root.val] + r
