# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def merge(one,two):
    
    if one==None and two==None:
        return None
        
    elif one==None:
        return two
    elif two==None:
        return one
    
    else:
        result=TreeNode()
        result.val=one.val+two.val
    
        result.left=merge(one.left,two.left)
        result.right=merge(one.right,two.right)
    
    
        return result

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        #result_tree=TreeNode()
        
        if t1==None and t2==None:
            return t1
        
        elif t1==None:
            return t2
        
        elif t2==None:
            return t1
        
        else:
            result=merge(t1,t2)
            return result    
    
