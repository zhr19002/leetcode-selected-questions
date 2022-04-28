class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree2list(root):
    lst = [None] * 7
    if root: 
        lst[0] = root.val
        if root.left: 
            lst[1] = root.left.val
            if root.left.left: 
                lst[3] = root.left.left.val
            if root.left.right: 
                lst[4] = root.left.right.val
        if root.right: 
            lst[2] = root.right.val
            if root.right.left: 
                lst[5] = root.right.left.val
            if root.right.right: 
                lst[6] = root.right.right.val
    else:
        return []
    return lst

class Solution:
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None

        root = TreeNode(postorder[-1])
        separator_idx = inorder.index(postorder[-1])
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[(separator_idx + 1):]
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):(len(postorder)-1)]
        
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        
        return root

s = Solution()
print(tree2list(s.buildTree([9,3,15,20,7], [9,15,7,20,3])))