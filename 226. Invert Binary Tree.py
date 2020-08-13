# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invert_func(node):
    temp=node.left
    node.left=node.right
    node.right=temp
    
    if node.left:
        invert_func(node.left)
    if node.right:
        invert_func(node.right)

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root==None:
            return None
        
        else:
            
            invert_func(root)
            
            
            
            return root
