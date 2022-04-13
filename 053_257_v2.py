from collections import deque

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
        stack = deque([root])
        path_stack = deque(str(root.val))
        result = []
        
        while stack:
            cur = stack.pop()
            path = path_stack.pop()
            if not (cur.left or cur.right):
                result.append(path)
            if cur.right:
                stack.append(cur.right)
                path_stack.append(path + '->' + str(cur.right.val))
            if cur.left:
                stack.append(cur.left)
                path_stack.append(path + '->' + str(cur.left.val))
        
        return result

s = Solution()
print(s.binaryTreePaths([1,2,3,None,5,None,None]))