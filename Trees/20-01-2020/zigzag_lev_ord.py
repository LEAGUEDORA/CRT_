# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def deep(node, level):
            while level >= len(res) : res.append([])
            res[level] += [node.val]
            if node.left : deep(node.left, level + 1)
            if node.right : deep(node.right, level + 1)
        
        if not root: return []
        res = []
        deep(root, 0)
        return [res[level] if not level % 2 else res[level][::-1] for level in range(len(res))  ]
