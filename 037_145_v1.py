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
    def postorderTraversal(self, lst):
        root = list2tree(lst)
        result = []
        
        def traversal(root):
            if root == None:
                return
            traversal(root.left)
            traversal(root.right)
            result.append(root.val)
        
        traversal(root)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.postorderTraversal([5,4,6,1,2,7,8]))
