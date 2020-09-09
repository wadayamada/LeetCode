# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        if len(nums)==0:
            return None
        
        root=TreeNode()
                
        
        def buildtree(node,sa):
            
            if len(sa)!=0:
                
                middle=int(len(sa)/2)                                
                node.val=sa[middle]
                
                sa_left=sa[:middle]
                sa_right=sa[middle+1:]                                
                
                if len(sa_left)!=0:                
                    node.left=TreeNode()
                    buildtree(node.left,sa_left)                    
                    
                if len(sa_right)!=0:
                    node.right=TreeNode()                                
                    buildtree(node.right,sa_right)                                                                                        
        
        buildtree(root,nums)                                            
            
        return root
