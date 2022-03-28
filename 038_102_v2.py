from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def list2tree(lst):
    root = TreeNode(lst[0])
    root.left = TreeNode(lst[1])
    root.right = TreeNode(lst[2])
    root.left.left = TreeNode(lst[3])
    root.left.right = TreeNode(lst[4])
    root.right.left = TreeNode(lst[5])
    root.right.right = TreeNode(lst[6])
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