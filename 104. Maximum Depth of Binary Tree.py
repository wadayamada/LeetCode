# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        else:
            return count_tree(root)
            
def count_tree(tree):
    if tree.left==None and tree.right==None:
        return 1
    elif tree.left==None:
        return 1+count_tree(tree.right)
    elif tree.right==None:
        return 1+count_tree(tree.left)
    else:
        return max(count_tree(tree.left),count_tree(tree.right))+1
