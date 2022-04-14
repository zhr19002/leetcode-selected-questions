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

class Solution:
    def isSameTree(self, p, q):
        p_root = list2tree(p)
        q_root = list2tree(q)
        return self.compare(p_root, q_root)
    
    def compare(self, tree1, tree2):
        if not tree1 and tree2:
            return False
        elif tree1 and not tree2:
            return False
        elif not tree1 and not tree2:
            return True
        elif tree1.val != tree2.val:
            return False       
        
        compareLeft = self.compare(tree1.left, tree2.left)
        compareRight = self.compare(tree1.right, tree2.right)
        isSame = compareLeft and compareRight
        
        return isSame

s = Solution()
print(s.isSameTree([1,2,2,3,4,4,3], [1,2,2,3,4,4,3]))
print(s.isSameTree([1,2,2,None,3,None,3], [1,2,2,3,4,4,3]))