# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def Treemax(node):
            if not node:
                return 0
            return 1 + max(Treemax(node.left), Treemax(node.right))

        def traverse(node):
            if not node:
                return True
            if  abs(Treemax(node.left) - Treemax(node.right)) > 1:
                return False  
            if not traverse(node.left):
                return False
            if not traverse(node.right):
                return False
            return True
        return traverse(root)
