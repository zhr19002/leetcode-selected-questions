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

if __name__ == '__main__':
    s = Solution()
    print(s.isSymmetric([1,2,2,3,4,4,3]))
    print(s.isSymmetric([1,2,2,None,3,None,3]))
