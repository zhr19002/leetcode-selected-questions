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
    def postorderTraversal(self, lst):
        root = list2tree(lst)
        stack = []
        result = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                stack.append(node)
                stack.append(None)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)     
            else:
                node = stack.pop()
                result.append(node.val)
        return result

s = Solution()
print(s.postorderTraversal([5,4,6,1,2,7,8]))