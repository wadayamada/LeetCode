# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:    
        
        if len(preorder)==0:
            return None
        
        root=TreeNode()
        
        def buildtree(node,p,i):
            
            node.val=p[0]
            
            ileft=i[:i.index(p[0])]
            iright=i[i.index(p[0])+1:]
                                
            pleft=p[1:1+len(ileft)]
            pright=p[1+len(ileft):]
            
            if len(ileft)!=0:
                node.left=TreeNode()
                buildtree(node.left,pleft,ileft)
                
            if len(iright)!=0:
                node.right=TreeNode()
                buildtree(node.right,pright,iright)
                
            
            
        
        buildtree(root,preorder,inorder)
        
        return root
        
