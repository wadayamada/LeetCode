# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right            
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
    
        if root==None:
            return 0
        
        self.ans=0
        
        def dia(node):
            if node==None:
                return 0
            
            left_length=dia(node.left)
            right_length=dia(node.right)
            self.ans=max(self.ans,left_length+right_length)
        
            return max(left_length,right_length)+1
        
        dia(root)
    
        return self.ans
