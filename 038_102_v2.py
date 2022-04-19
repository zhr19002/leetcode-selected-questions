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
    def levelOrder(self, lst):
        root = list2tree(lst)
        result = []
        def helper(root, depth):
            if root == None:
                return []
            if len(result) == depth:
                result.append([])
            result[depth].append(root.val)
            if root.left:
                helper(root.left, depth + 1)
            if root.right:
                helper(root.right, depth + 1)
        helper(root, 0)
        return result

s = Solution()
print(s.levelOrder([3,9,20,None,None,15,7]))
