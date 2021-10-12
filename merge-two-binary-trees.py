# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
       
    # Approach 1
        if root1 is None: 
            return root2
        que = [(root1,root2)]
        while que: 
            node1,node2 = que.pop()
            if node1 is None or node2 is None:
                continue
            node1.val += node2.val
            if node1.left is None: 
                node1.left = node2.left 
            else: 
                que.append((node1.left,node2.left))
            if node1.right is None: 
                node1.right = node2.right 
            else: 
                que.append((node1.right,node2.right))
        return root1
            
            
        
        
# Approach 2 
        def dfs(node1, node2):
            if node1 is None and node2 is None: 
                return None
            if node1 is None: 
                return node2 
            if node2 is None: 
                return node1 
            node1.val += node2.val 
            node1.left = dfs(node1.left, node2.left)
            node1.right = dfs(node1.right,node2.right)
            return node1
        return dfs(root1,root2)
