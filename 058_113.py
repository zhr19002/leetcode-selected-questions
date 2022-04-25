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
    def pathsum(self, lst, targetsum):
        root = list2tree(lst)
        def traversal(root, remain):
            if (not root.left) and (not root.right):
                if remain == 0:
                    result.append(path[:])
                return
            
            if root.left:
                remain -= root.left.val
                path.append(root.left.val)
                traversal(root.left, remain)
                remain += root.left.val
                path.pop()
            if root.right:
                remain -= root.right.val
                path.append(root.right.val)
                traversal(root.right, remain)
                remain += root.right.val
                path.pop()

        result, path = [], []
        if root == None:
            return []
        path.append(root.val)
        traversal(root, targetsum - root.val)
        return result

s = Solution()
print(s.pathsum([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1], 22))