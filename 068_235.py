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

def val2tree(lst, node):
    root = list2tree(lst)
    if lst[0] == node.val: node = root
    if lst[1] == node.val: node = root.left
    if lst[2] == node.val: node = root.right
    if lst[3] == node.val: node = root.left.left
    if lst[4] == node.val: node = root.left.right
    if lst[5] == node.val: node = root.right.left
    if lst[6] == node.val: node = root.right.right
    if lst[7] == node.val: node = root.left.left.left
    if lst[8] == node.val: node = root.left.left.right
    if lst[9] == node.val: node = root.left.right.left
    if lst[10] == node.val: node = root.left.right.right
    if lst[11] == node.val: node = root.right.left.left
    if lst[12] == node.val: node = root.right.left.right
    if lst[13] == node.val: node = root.right.right.left
    if lst[14] == node.val: node = root.right.right.right
    return node

class Solution:    
    def LCA(self, lst, p, q):
        root = list2tree(lst)
        p = val2tree(lst, TreeNode(p))
        q = val2tree(lst, TreeNode(q))
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root.val

s = Solution()
print(s.LCA([6,2,8,0,4,7,9,None,None,3,5,None,None,None,None], 2, 8))
print(s.LCA([6,2,8,0,4,7,9,None,None,3,5,None,None,None,None], 2, 4))