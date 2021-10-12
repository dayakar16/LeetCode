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
        if not root: 
            return None 
        que = [root]
        while que:
            que_2 = []
            ln = len(que)
            for i in range(ln): 
                if i == ln -1: 
                    que[i].next = None
                else: 
                    que[i].next = que[i+1]
                if que[i].left is not None: 
                    que_2.append(que[i].left)
                if que[i].right is not None: 
                    que_2.append(que[i].right)
            que = que_2
        return root
