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
    def isSymmetric(self, lst):
        root = list2tree(lst)
        if not root:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)        
        while stack:
            leftNode = stack.pop()
            rightNode = stack.pop()
            if not leftNode and not rightNode:
                continue
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            stack.append(leftNode.left)
            stack.append(rightNode.right)
            stack.append(leftNode.right)
            stack.append(rightNode.left)
        return True

s = Solution()
print(s.isSymmetric([1,2,2,3,4,4,3]))
print(s.isSymmetric([1,2,2,None,3,None,3]))