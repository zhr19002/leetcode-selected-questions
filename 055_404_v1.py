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
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        
        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right)
        
        cur_left_leaf_val = 0
        if root.left and not root.left.left and not root.left.right:
            cur_left_leaf_val = root.left.val
        
        return cur_left_leaf_val + left_left_leaves_sum + right_left_leaves_sum

s = Solution()
print(s.sumOfLeftLeaves(list2tree([3,9,20,None,None,15,7])))