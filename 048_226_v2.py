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
        if not root:
            return []
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            temp = node.left
            node.left = node.right
            node.right = temp
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

s = Solution()
print(s.invertTree([4,2,7,1,3,6,9]))