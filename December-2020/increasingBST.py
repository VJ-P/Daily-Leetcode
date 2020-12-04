# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root == None: return None
        nodes = []
        def helper(node):
            if node.left: helper(node.left)
            nodes.append(node)
            if node.right: helper(node.right)
        
        helper(root)
        newRoot = nodes.pop(0)
        curr = newRoot
        while len(nodes) > 0:
            curr.left = None
            curr.right = nodes.pop(0)
            curr = curr.right
        curr.left = None
        curr.right = None
        return newRoot