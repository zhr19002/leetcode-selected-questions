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
    def rob(self, lst):
        root = list2tree(lst)
        result = self.rob_tree(root)
        return max(result[0], result[1])
        
    def rob_tree(self, root):
        if root == None:
            return (0, 0)
        left = self.rob_tree(root.left)
        right = self.rob_tree(root.right)
        val1 = max(left[0], left[1]) + max(right[0], right[1])
        val2 = root.val + left[0] + right[0]
        return (val1, val2)

s = Solution()
print(s.rob([3,2,3,None,3,None,1]))
print(s.rob([3,4,5,1,3,None,1]))