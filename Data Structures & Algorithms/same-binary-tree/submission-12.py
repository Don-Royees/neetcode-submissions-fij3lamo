# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node , node2):
            if not (node and node2):
                return False  
            if node.val != node2.val:
                return False    
            if node.left or node2.left:
                if not (node.left and node2.left):
                    return False    
                return traverse(node.left , node2.left)          
            if node.right or node2.right:
                if not (node.right and node2.right):
                    return False
                return traverse(node.right , node2.right)       
            print(node.val , node2.val)        
            return True
        if not q and not p:
            return True    
        return traverse(p,q)           

