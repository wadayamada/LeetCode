# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        result={}
        
        if root==None:
            return result
        
        
        
        def func(node,depth):
            
            if not depth in result:
                result[depth]=[]
            
            if depth%2==0:
                result[depth].append(node.val)
                
            else:
                result[depth].insert(0,node.val)
                
            if not node.left==None:
                func(node.left,depth+1)
                
            if not node.right==None:
                func(node.right,depth+1)
                
            
            
        func(root,0)
            
        return [result[key] for key in result]
