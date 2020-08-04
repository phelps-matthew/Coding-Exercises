# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Do an in order traversal, deleting any nodes beyond range
# Now just need to shift root around
# Can't do general BST deletion method as it requires parent
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        for p in self.inorder(root):
            print(p)
            if p.val <= L:
                # trim left children
                p.left = None
                if p.val < L:
                    # become right child
                    self.set_node(p, p.right)
            if p.val >= R:
                # trim right children
                p.right = None
                if p.val > R:
                    # become left child
                    self.set_node(p, p.left)
            print(root)
            print('-'*10)
        return root
    
    def inorder(self, p):
        """traverse subtree rooted at p"""
        # traverse left subtree
        if p.left:
            # kind of behaves like a stack, the yields pass through the "nested" for loops
            for x in self.inorder(p.left):
                yield x
        # Visit p
        yield p
        # traverse right subtree
        if p.right:
            for x in self.inorder(p.right):
                yield x
    
    def set_node(self, p, q):
        if p and q:
            p.val = q.val
            p.left = q.left
            p.right = q.right
        return p
