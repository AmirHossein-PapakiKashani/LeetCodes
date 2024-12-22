class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.search(val)
    
    def search(self,treeNod : TreeNode , data):
        # Base case: If the tree is empty, the data is not found
        if treeNod is None:
            return None

        # If the data matches the current node's value, return the node
        if data == self.val:
            return self

        # If the data is less than the current node's value, search in the left subtree
        if data < self.val:
            return self.left.search(data) if self.left else None

        # If the data is greater than the current node's value, search in the right subtree
        return self.right.search(data) if self.right else None
     
root = TreeNode(10)
root.insert(5)
root.insert(15)
root.insert(3)
root.insert(7)
root.insert(12)
root.insert(20)
result = Solution()
a = result.searchBST(root, 3)
rr = []
rr.append(a.val)
rr.append(a.right)
rr.append(a.left)
print(a)