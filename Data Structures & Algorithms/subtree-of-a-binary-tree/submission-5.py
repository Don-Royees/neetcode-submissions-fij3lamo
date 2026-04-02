# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q: # Both are None
                return True
            if not p or not q:  # One is None, the other isn't
                return False
            if p.val != q.val:  # Values don't match
                return False
            # Check both children and return the combined result
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        # Main function to search through the big tree
        if not root: 
            return False
        
        # 1. Is the current node the start of the subRoot?
        if isSameTree(root, subRoot):
            return True
            
        # 2. If not, look in the left child OR the right child
        # We use 'or' because we only need to find it once!
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)