# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def godown(node, level):
            if not node:
                return
            if len(self.result) <= level:
                self.result.append([])
            self.result[level].append(node.val)
            
            godown(node.left, level + 1)
            godown(node.right, level + 1)       
        self.result = []
        godown(root, 0)
        
        return self.result
