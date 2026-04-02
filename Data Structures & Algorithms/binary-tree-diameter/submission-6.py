# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest=[]
        def maxTree(node):
            if not node:
                return 0
            return 1 + max(maxTree(node.left), maxTree(node.right))    
        def treeNodeTraverse(node):
            if not node:
                return 0 
            maxRight = maxTree(node.right)
            maxLeft = maxTree(node.left)
            print(maxTree(root))
            largest.append(maxRight + maxLeft)
            if node.left:
                treeNodeTraverse(node.left)
            if node.right:
                treeNodeTraverse(node.right)
            return max(largest)
        largest.append(maxTree(root) - 1)
        return treeNodeTraverse(root)          

