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
    def invertTree(self, lst):
        root = list2tree(lst)
        result = []
        
        def traversal(root):
            if root == None:
                return result
            temp = root.left
            root.left = root.right
            root.right = temp
            result.append(root.val)
            traversal(root.left)
            traversal(root.right)
        
        traversal(root)
        return result

s = Solution()
print(s.invertTree([4,2,7,1,3,6,9]))