class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def list2tree(lst):
    if lst[0] != None: root = TreeNode(lst[0])  
    if lst[1] != None: root.left = TreeNode(lst[1])
    if lst[2] != None: root.right = TreeNode(lst[2])
    if lst[3] != None: root.left.left = TreeNode(lst[3])
    if lst[4] != None: root.left.right = TreeNode(lst[4])
    if lst[5] != None: root.right.left = TreeNode(lst[5])
    if lst[6] != None: root.right.right = TreeNode(lst[6])
    if lst[7] != None: root.left.left.left = TreeNode(lst[7])
    if lst[8] != None: root.left.left.right = TreeNode(lst[8])
    if lst[9] != None: root.left.right.left = TreeNode(lst[9])
    if lst[10] != None: root.left.right.right = TreeNode(lst[10])
    if lst[11] != None: root.right.left.left = TreeNode(lst[11])
    if lst[12] != None: root.right.left.right = TreeNode(lst[12])
    if lst[13] != None: root.right.right.left = TreeNode(lst[13])
    if lst[14] != None: root.right.right.right = TreeNode(lst[14])
    return root

class Solution:    
    def insertIntoBST(self, lst, val):
        root = list2tree(lst)
        return self.insertBST(root, val).val
        
    def insertBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        if root.val > val:
            root.left = self.insertBST(root.left, val)
        if root.val < val:
            root.right = self.insertBST(root.right, val)
        
        return root

s = Solution()
print(s.insertIntoBST([4,2,7,1,3,None,None,None,None,None,None,None,None,None,None], 5))