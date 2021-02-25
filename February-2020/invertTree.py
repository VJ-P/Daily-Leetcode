# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            node.left, node.right = node.right, node.left
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        if root:
            dfs(root)
        return root