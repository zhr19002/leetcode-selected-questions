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

def tree2list(root):
    lst = [None] * 15
    if root: 
        lst[0] = root.val
        if root.left: 
            lst[1] = root.left.val
            if root.left.left: 
                lst[3] = root.left.left.val
                if root.left.left.left: 
                    lst[7] = root.left.left.left.val
                if root.left.left.right: 
                    lst[8] = root.left.left.right.val
            if root.left.right: 
                lst[4] = root.left.right.val
                if root.left.right.left: 
                    lst[9] = root.left.right.left.val
                if root.left.right.right: 
                    lst[10] = root.left.right.right.val
        if root.right: 
            lst[2] = root.right.val
            if root.right.left: 
                lst[5] = root.right.left.val
                if root.right.left.left: 
                    lst[11] = root.right.left.left.val
                if root.right.left.right: 
                    lst[12] = root.right.left.right.val
            if root.right.right: 
                lst[6] = root.right.right.val
                if root.right.right.left: 
                    lst[13] = root.right.right.left.val
                if root.right.right.right: 
                    lst[14] = root.right.right.right.val
    else:
        return []
    return lst

class Solution:
    def __init__(self):
        self.pre = TreeNode(0)
    
    def convertBST(self, lst):
        root = list2tree(lst)
        self.traversal(root)
        return root
    
    def traversal(self, root):
        if not root:
            return None
        
        self.traversal(root.right)
        root.val += self.pre.val
        self.pre = root
        self.traversal(root.left)

s = Solution()
print(tree2list(s.convertBST([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])))