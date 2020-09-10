# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root==None:
            return 0                
        
        def depth_cal(node):
            
            if node.left==None and node.right==None:
                return 1                        
            
            elif node.left==None:
                return depth_cal(node.right)+1
            
            elif node.right==None:
                return depth_cal(node.left)+1
            
            else:                    
                return min(depth_cal(node.left),depth_cal(node.right))+1                                    
        
        
        return depth_cal(root)
