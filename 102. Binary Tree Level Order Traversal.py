# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        result_dict={}
        
        if root==None:
            return []
                        
        def func(node,depth):
            
            if not depth in result_dict:
                result_dict[depth]=[]
            
            result_dict[depth].append(node.val)
            
            if not node.left==None:
                func(node.left,depth+1)
            
            if not node.right==None:
                func(node.right,depth+1)
                                                        
        func(root,0)
        
        return [result_dict[key] for key in sorted(result_dict)]
        
