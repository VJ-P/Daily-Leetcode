# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower, upper):
            if node.left != None:
                helper(node.left, lower, node.val)
            
            if node.val >= upper or node.val <= lower:
                ans[0] = False
            
            if node.right != None:
                helper(node.right, node.val, upper)
        
        ans = [True]
        helper(root, float('-inf'), float('inf'))
        return ans[0]