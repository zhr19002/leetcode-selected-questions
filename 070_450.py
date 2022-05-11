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
    return root

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
    def deleteNode(self, lst, key):
        root = list2tree(lst)
        return self.delete(root, key)
        
    def delete(self, root, key):
        if not root:
            return None
        
        if root.val == key:
            if not root.left and not root.right:
                del root
                return None
            if not root.left and root.right:
                tmp = root
                root = root.right
                del tmp
                return root
            if root.left and not root.right:
                tmp = root
                root = root.left
                del tmp
                return root
            else:
                v = root.right
                while v.left:
                    v = v.left
                v.left = root.left
                tmp = root
                root = root.right
                del tmp
                return root
        
        if root.val > key:
            root.left = self.delete(root.left, key)
        if root.val < key:
            root.right = self.delete(root.right, key)
        return root

s = Solution()
print(tree2list(s.deleteNode([5,3,6,2,4,None,7], 3)))