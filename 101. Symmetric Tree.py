# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        else:
            return self.symmetric_check(root.left,root.right)
        
    def symmetric_check(self,left,right):
        if left==None and right==None:
            return True
        elif left==None or right==None:
            return False
        else:
            if left.val==right.val:
                #左の木の左と、右の木の右が同じで、かつ、左の木の右と、右の木の左が同じ、ことを確かめる
                return self.symmetric_check(left.left,right.right) and self.symmetric_check(left.right,right.left)
            
            else:
                return False
