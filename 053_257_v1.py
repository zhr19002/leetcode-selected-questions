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
    def binaryTreePaths(self, lst):
        root = list2tree(lst)
        path = ''
        result = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result
        
    def traversal(self, cur, path, result):
        path += str(cur.val)
        if not cur.left and not cur.right:
            result.append(path)
        if cur.left:
            self.traversal(cur.left, path + '->', result)
        if cur.right:
            self.traversal(cur.right, path + '->', result)

s = Solution()
print(s.binaryTreePaths([1,2,3,None,5,None,None]))