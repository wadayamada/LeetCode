# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if root==None:
            return False
        
        def check(node,number):
            
            if node.left==None and node.right==None:
                if node.val==number:
                    return True
                else:
                    return False
                
            elif node.left==None:
                return check(node.right,number-node.val)
            
            elif node.right==None:
                return check(node.left,number-node.val)
            
            else:
                return check(node.left,number-node.val) or check(node.right,number-node.val)
            
            
        return check(root,sum)
