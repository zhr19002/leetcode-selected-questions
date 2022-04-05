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
        return self.compare(root.left, root.right)
    
    def compare(self, left, right):
        if left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left == None and right == None:
            return True
        elif left.val != right.val:
            return False       
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        isSame = outside and inside
        return isSame

s = Solution()
print(s.isSymmetric([1,2,2,3,4,4,3]))
print(s.isSymmetric([1,2,2,None,3,None,3]))