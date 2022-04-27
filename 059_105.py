class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree2list(root):
    lst = [None] * 7
    if root:
        lst[0] = root.val
    else:
        return []
    if root.left: lst[1] = root.left.val
    if root.right: lst[2] = root.right.val
    if root.left.left: lst[3] = root.left.left.val
    if root.left.right: lst[4] = root.left.right.val
    if root.right.left: lst[5] = root.right.left.val
    if root.right.right: lst[6] = root.right.right.val
    return lst

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        separator_idx = inorder.index(preorder[0])
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[(separator_idx + 1):]
        preorder_left = preorder[1:(1 + len(inorder_left))]
        preorder_right = preorder[(1 + len(inorder_left)):]
        
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root

s = Solution()
print(tree2list(s.buildTree([3,9,20,15,7], [9,3,15,20,7])))