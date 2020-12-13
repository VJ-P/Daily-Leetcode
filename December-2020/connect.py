"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None: return None
        queue = [root]
        while len(queue) > 0:
            k = len(queue)
            for i in range(k):
                popped = queue.pop(0)
                if i == k-1:
                    popped.next = None
                else:
                    popped.next = queue[0]
                
                if popped.left != None:
                    queue.append(popped.left)
                if popped.right != None:
                    queue.append(popped.right)
        return root