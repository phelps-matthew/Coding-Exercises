# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Tried doing an in order traversal, deleting any nodes beyond range, logic 
# became too convoluted and non-functional
# Can't do general BST deletion method as it requires parent
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root
    
# above acts like a filter, recursively passing only values within the range
# depth first, integrated with operations
# note by conditionals that end of recursion stack only hits when None, or within [L,R]. In other
# words, the only returns are None or [L, R]. These returns are used to reassign root.left and root.right for valid roots
# Going top down, skips over bad roots (will not return them at least), however bad node connection to good child node still exists
# Very difficult to have thought of implementing; more practice needed
