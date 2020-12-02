# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None: return 0
        ans = 0
        queue = [root]
        while len(queue) > 0:
            ans += 1
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
        return ans