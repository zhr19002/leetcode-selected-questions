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
    def isBalanced(self, lst):
        root = list2tree(lst)
        if self.get_height(root) != -1:
            return True
        else:
            return False
    
    def get_height(self, root):
        if not root:
            return 0
        left_height = self.get_height(root.left)
        if left_height == -1:
            return -1
        right_height = self.get_height(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)

if __name__ == '__main__':
    s = Solution()
    print(s.isBalanced([3,9,20,None,None,15,7,None,None,None,None,None,None,None,None]))
    print(s.isBalanced([1,2,2,3,3,None,None,4,4,None,None,None,None,None,None]))
