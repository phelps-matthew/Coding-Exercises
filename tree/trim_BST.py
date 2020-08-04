# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Do an in order traversal, deleting any nodes beyond range
# Now just need to shift root around
# Can't do general deletion method as it requires parent
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        for p in self.inorder(root):
            if p.left and p.left.val < L:
                p.left = p.left.right
            if p.right and p.right.val > R:
                p.right = p.right.left
        return root
    
    def inorder(self, p):
        """traverse subtree rooted at p"""
        # traverse left subtree
        if p.left:
            # kind of behaves like a stack, the yields pass through the "nested" for loops
            for x in self.inorder(p.left):
                yield x
        # Visit p (will be root)
        yield p
        # traverse right subtree
        if p.right:
            for x in self.inorder(p.right):
                yield x     
