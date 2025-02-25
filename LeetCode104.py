class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self,root):
  
        # Base case: if null
        if root is None:
            return       
        # Recur on the left subtree
        self.inorderTraversal(root.left)
        # Recur on the right subtree
        self.inorderTraversal(root.right)
    def maxDepth(self, root: TreeNode) -> int:
        